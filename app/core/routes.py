from flask import Blueprint, jsonify, request

from app.core.models import Member
from app.extensions import db

member_blueprint = Blueprint("members", __name__)


@member_blueprint.route("/members")
def members():
    all_members = Member.query.all()
    members = []

    for member in all_members:
        member_dict = {}
        member_dict['name'] = member.name
        member_dict['last_name'] = member.last_name
        member_dict['email'] = member.email
        member_dict['roll'] = member.roll
        members.append(member_dict)

    return jsonify({'members': members})


@member_blueprint.route("/member/<int:member_id>", methods=['GET'])
def member(member_id):
    member = Member.query.get_or_404(member_id)
    data = {
        'name': member.name,
        'last_name': member.last_name,
        'email': member.email,
        'roll': member.roll
    }
    return jsonify(data)


@member_blueprint.route("/member/<int:member_id>/update", methods=['PUT', 'PATCH'])
def member_update(member_id):
    data = request.get_json()
    member = Member.query.get_or_404(member_id)
    member.name = data['name']
    member.last_name = data['last_name']
    member.email = data['email']
    member.roll = data['roll']
    db.session.commit()

    data = {
        'name': member.name,
        'last_name': member.last_name,
        'email': member.email,
        'roll': member.roll
    }
    return jsonify(data)


@member_blueprint.route("/member/create", methods=["POST"])
def member_create():
    data = request.get_json()

    name = data["name"]
    last_name = data["last_name"]
    email = data["email"]
    roll = data["roll"]

    member = Member(name=name, last_name=last_name, email=email, roll=roll)
    db.session.add(member)
    db.session.commit()
    member_data = Member.query.get(member.id)

    return jsonify(
        {
            'name': member_data.name,
            'last_name': member_data.last_name,
            'email': member_data.email,
            'roll': member_data.roll,
        }
    )


@member_blueprint.route("/member/<int:member_id>/delete", methods=['POST'])
def member_delete(member_id):
    member = Member.query.get_or_404(member_id)
    db.session.delete(member)
    db.session.commit()
    return jsonify({'message': 'Member has been deleted..'})

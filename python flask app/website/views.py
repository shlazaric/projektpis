from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')  # Gets the note from the HTML

        if len(note) < 1:
            flash('Biljeska (obaveza) je prekratka!', category='error')
        else:
            # providing the schema for the note
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)  # adding the note to the database
            db.session.commit()
            flash('Obaveza dodana!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-note', methods=['POST'])
def delete_note():

    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

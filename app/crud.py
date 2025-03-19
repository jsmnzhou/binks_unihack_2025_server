from flask import Flask, request, jsonify
import os
from supabase import create_client, Client

SUPABASE_URL = os.getenv('SUPABASE_URL')
VITE_ANON_KEY = os.getenv('VITE_ANON_KEY')
supabase: Client = create_client(SUPABASE_URL, VITE_ANON_KEY)

def create_assessment(data):
    response = supabase.table('assessments').insert({'class_name': data}).execute()
    if response.status_code != 201:
        return jsonify({'error': 'Failed to insert into Supabase', 'details': response.data}), 500

    return jsonify({'message': 'Class created successfully', 'data': response.data}), 201

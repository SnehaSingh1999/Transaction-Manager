from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import csv

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///transactions.db'
db = SQLAlchemy(app)
class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    amount = db.Column(db.Float)
    
    def serialize(self):
        return{
            'id' : self.id,
            'name' : self.name,
            'amount' : self.amount,
        }



@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.csv'):
        csv_data = file.read().decode('utf-8')
        csv_reader = csv.reader(csv_data.splitlines(), delimiter=',')
        headers = next(csv_reader)  # Assuming the first row is headers
        
        for row in csv_reader:
            transaction = Transaction(
                name=row[0],  
                amount=float(row[1])
            ),
            db.session.add(transaction)
        
        db.session.commit()
        return jsonify({'message': 'File uploaded and data inserted successfully'}), 200
    
    return jsonify({'error': 'Invalid file format, only CSV files are allowed'}), 400

@app.route('/transactions', methods=['GET'])
def get_transactions():
    transactions = Transaction.query.all()
    serialized_transactions = [transaction.serialize() for transaction in transactions]
    return jsonify(serialized_transactions), 200

@app.route('/transactions/<int:transaction_id>', methods=['PUT'])
def update_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'error': 'Transaction not found'}), 404
        
    data = request.get_json()
    transaction.name = data.get('name', transaction.name)
    transaction.amount = data.get('amount', transaction.amount)
    db.session.commit()
    return jsonify({'message': 'Transaction updated successfully'}), 200

@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    transaction = Transaction.query.get(transaction_id)
    if not transaction:
        return jsonify({'error': 'Transaction not found'}), 404
    
    db.session.delete(transaction)
    db.session.commit()
    return jsonify({'message': 'Transaction deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)

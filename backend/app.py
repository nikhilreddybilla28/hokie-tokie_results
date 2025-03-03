from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Replace with your actual file paths
csv1_path = '/efs/home/nikilr/CodeGen-Blue-Team/eval/code_utilityv1.csv'
csv2_path = '/efs/home/nikilr/CodeGen-Blue-Team/eval/results.csv'

@app.route('/code_utilityv1.csv', methods=['GET'])
def code_utilityv1():
    try:
        df = pd.read_csv(csv1_path)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/results.csv', methods=['GET'])
def results():
    try:
        df = pd.read_csv(csv2_path)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

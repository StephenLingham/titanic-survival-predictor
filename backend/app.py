from flask import Flask, request, jsonify
from flask_cors import CORS
import machineLearning
import mongoService

machineLearning.trainModel()

app = Flask(__name__)
CORS(app)

@app.route('/api/predict', methods=['POST'])
def predict():
    content = request.json
    
    passengerClass = content['passengerClass']
    male = content['male']
    age = content['age']

    survived = machineLearning.predictSurvived(passengerClass, male, age)
    survivedProbability = machineLearning.predictSurvivedProbability(passengerClass, male, age)

    stats = {
        "passengerClass": passengerClass,
        "male": male,
        "age": age,
        "survived": survived,
        "survivedProbability": survivedProbability
    }

    mongoService.add(stats)

    responseDictionary = {
        "survived": survived,
        "survivedProbability": survivedProbability
    }

    responseJson = jsonify(responseDictionary)

    return responseJson

@app.route('/api/stats', methods=['GET'])
def getStats():
    mongoService.printAll()

    allUserData = mongoService.getAll()

    numberOfUsers = len(allUserData)

    usersWhoSurvived = list(filter(lambda user : user["survived"] == 1, allUserData))

    numberOfUsersWhoSurvived = len(usersWhoSurvived)
    
    responseDictionary = {
        "totalNumberOfUsers": numberOfUsers,
        "numberOfUsersWhoSurvived": numberOfUsersWhoSurvived
    }

    responseJson = jsonify(responseDictionary)

    return responseJson

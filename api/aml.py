from rest_framework.decorators import api_view, permission_classes
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from rest_framework.permissions import IsAuthenticated
from .models import AML

@api_view(['POST'])
@csrf_exempt
# @permission_classes([IsAuthenticated])

def insertAMLInfo(request):
	amlJsonData = json.loads(request.body)
	try:
		AML.objects.create(
			first_name = amlJsonData['data']['first_name'],
			last_name = amlJsonData['data']['last_name'],
			date_of_birth = amlJsonData['data']['date_of_birth'],
			nationality = amlJsonData['data']['nationality'],
			email = amlJsonData['email'],
			gender = amlJsonData['data']['gender'],
			currentStatus = amlJsonData['aml_result']['currentstatus'],
			riskLevelSummary = amlJsonData['aml_result']['risk_level_summary'],
			riskLevel = amlJsonData['aml_result']['matches'][0]['risk_level'],
			riskIcon = amlJsonData['aml_result']['matches'][0]['risk_icon'],
			amlID = amlJsonData['id'],
			webhook_trigger = amlJsonData['webhook_trigger']
		)
		response = {
			"success": True
		}
		return JsonResponse(response)
	except:
		response = {
			"success": False
		}
		return JsonResponse(response)

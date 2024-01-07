from django.shortcuts import render
from .models import Toad, Requests
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def toad_detail(request, toad_id):
    toad = Toad.objects.get(id=toad_id)
    return render(request, 'toad_detail.html', {'toad': toad})

@csrf_exempt
def send_request_view(request, toad_id, curr_toad):
    # Retrieve the Toad object based on the provided toad_id
    toad_to = Toad.objects.get(id=toad_id)
    toad_from = Toad.objects.get(id=curr_toad)
    # Invoke the send_request model method
    success = toad_from.send_request(toad_to)

    if success:
        # Perform any additional actions or return a success response
        return HttpResponse("Request sent successfully.")
    else:
        # Handle the case where the request failed
        return HttpResponse("Failed to send request.")


@csrf_exempt
def accept_request_view(request, toad_id, curr_toad):
    # Retrieve the Toad object based on the provided toad_id
    toad_from = Toad.objects.get(id=toad_id)
    toad_to = Toad.objects.get(id=curr_toad)
    print("IM HERE")
    # Invoke the send_request model method
    success = toad_to.accept_request(toad_from)

    if success:
        # Perform any additional actions or return a success response
        return HttpResponse("Request sent successfully.")
    else:
        # Handle the case where the request failed
        return HttpResponse("Failed to send request.")


def check_requests_view(request, toad_id):
    if request.method == 'GET':
        # Assuming you have the current Toad object available
        current_toad = Toad.objects.get(id=toad_id)

        try:
            request_objs = current_toad.check_requests()
            print(request_objs.all())
            # Create a list to hold the request information
            requests_data = []
            
            for request_obj in request_objs:
                # Retrieve the relevant information from each request object
                request_it = {
                    'request_from': request_obj.request_from.name,
                    'accepted': request_obj.accepted,
                    'ignore': request_obj.ignore
                }
                
                # Append the request data to the list
                requests_data.append(request_it)
            print(requests_data)
            if requests_data:
                # Return the list of request data
                return JsonResponse(requests_data, safe=False)
            else:
                return JsonResponse({'error': 'No requests found.'}, status=404)
        except Requests.DoesNotExist:
            return JsonResponse({'error': 'No requests found.'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method.'}, status=400)
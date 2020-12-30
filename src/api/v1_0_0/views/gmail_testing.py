from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from googleapiclient.discovery import build

from utils.gmail_quickstart import get_creds


class GmailViewSet(GenericViewSet,):

    @action(detail=False, methods=('get', ), url_path='testing-gmail')
    def get_testing_gmail(self, request):

        creds = get_creds()
        service = build('gmail', 'v1', credentials=creds)

        # # Call the Gmail API
        results = service.users().labels().list(userId='me').execute()
        labels = results.get('labels', [])
        return Response(labels)

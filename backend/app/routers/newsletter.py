from fastapi import APIRouter, Depends, HTTPException
from app.models.book import NewsletterSubscriptionRequest, NewsletterSubscriptionResponse

router = APIRouter(prefix="/api/newsletter", tags=["newsletter"])

# Por ahora, servicio mock simple. En el futuro, esto sería un servicio de dominio
# con su puerto y adaptadores correspondientes.

@router.post("/subscribe", response_model=NewsletterSubscriptionResponse)
async def subscribe_newsletter(subscription: NewsletterSubscriptionRequest):
    """
    Suscribe un email al newsletter.

    - **email**: Email válido para suscribir
    """
    try:
        # Aquí iría la lógica de negocio real
        # Por ahora, solo simulamos el proceso
        print(f"New newsletter subscriber: {subscription.email}")

        # En un futuro, esto usaría:
        # newsletter_service = get_newsletter_service()
        # result = newsletter_service.subscribe(subscription.email)

        return NewsletterSubscriptionResponse(
            status="success",
            message=f"Successfully subscribed {subscription.email}"
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Error subscribing to newsletter: {str(e)}"
        )
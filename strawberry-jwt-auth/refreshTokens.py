from django.db import models
from django.conf import settings


class RefreshTokens(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    refreshToken = models.CharField(max_length=255)
    issued = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "refreshTokens"
        verbose_name_plural = "Refresh Tokens"
        verbose_name = "Refresh Token"

    def __str__(self):
        return self.refreshToken


__all__ = [
    'RefreshTokens'
]

from sqlalchemy import Column, Boolean, Integer, DateTime, ForeignKey, Text
from sqlalchemy.dialects.postgresql import UUID
from datetime import datetime
import uuid

from goodbug.core.database import Base


class ProductImage(Base):
    __tablename__ = "product_images"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    product_id = Column(
        UUID(as_uuid=True),
        ForeignKey("products.id", ondelete="CASCADE"),
        nullable=False
    )

    image_url = Column(Text, nullable=False)
    is_primary = Column(Boolean, default=False)
    position = Column(Integer, default=1)

    created_at = Column(DateTime, default=datetime.utcnow)

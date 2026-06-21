from django.core.management.base import BaseCommand
from core.models import Department
from waste_management.models import WasteCategory


class Command(BaseCommand):
    help = "Bootstrap ERP system (Departments + Waste Categories)"

    def handle(self, *args, **kwargs):

        # =========================
        # 1. DEPARTMENTS
        # =========================
        departments = [
            "waste",
            "inventory",
            "finance",
            "hr",
            "admin",
            "collection"
        ]

        for d in departments:
            obj, created = Department.objects.get_or_create(name=d)
            self.stdout.write(self.style.SUCCESS(
                f"Department: {d} {'CREATED' if created else 'EXISTS'}"
            ))

        # =========================
        # 2. WASTE CATEGORIES
        # =========================
        categories = [
            "Plastics",
            "Metals",
            "Paper",
            "Glass",
            "Organic",
            "Rubber",
            "E-waste"
        ]

        for c in categories:
            obj, created = WasteCategory.objects.get_or_create(name=c)
            self.stdout.write(self.style.SUCCESS(
                f"Category: {c} {'CREATED' if created else 'EXISTS'}"
            ))

        self.stdout.write(self.style.SUCCESS(
            "\n🚀 ERP Bootstrap Completed Successfully (No Suppliers Created)"
        ))
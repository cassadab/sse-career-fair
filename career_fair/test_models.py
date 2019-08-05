from django.test import TestCase
from career_fair.models import JobType


class JobTypeTest(TestCase):

    def test_job_entry(self):
        job = JobType(job_name="Tester")
        job.save()
        actual_job = JobType.objects.get(job_name="Tester")
        self.assertEqual(1, JobType.objects.count())
        self.assertEqual(job.job_name, actual_job.job_name)

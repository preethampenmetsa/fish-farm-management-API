from .models import Sampling

class SamplingService:

    @staticmethod
    def get_previous_sampling(sampling):
        return Sampling.objects.filter(
            stocking=sampling.stocking,
            sample_date__lt=sampling.sample_date
        ).order_by('-sample_date').first()

    @staticmethod
    def calculate_growth(sampling):
        previous = SamplingService.get_previous_sampling(sampling)

        if previous:
            return sampling.average_weight - previous.average_weight

        # fallback to initial stocking avg size
        initial_weight = sampling.stocking.avg_size
        if initial_weight:
            return sampling.average_weight - initial_weight

        return None
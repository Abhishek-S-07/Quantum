"""
===========================================================
QuantumSecureNet

Quantum Communication Health Monitor (QCHM)

This module evaluates the health of a BB84 quantum
communication channel using the Quantum Bit Error Rate (QBER).

The QCHM is a rule-based decision support system.
It does NOT modify the BB84 protocol.

===========================================================
"""

from dataclasses import dataclass


@dataclass
class HealthReport:
    """
    Stores the health evaluation results.
    """

    qber: float
    status: str
    recommendation: str
    color: str
    secure: bool


class QuantumCommunicationHealthMonitor:
    """
    Rule-based Quantum Communication Health Monitor.
    """

    def __init__(
        self,
        secure_threshold: float = 5.0,
        warning_threshold: float = 11.0,
    ):

        self.secure_threshold = secure_threshold
        self.warning_threshold = warning_threshold

    def evaluate(self, qber: float) -> HealthReport:
        """
        Evaluate the communication channel using QBER.
        """

        if qber <= self.secure_threshold:

            return HealthReport(

                qber=qber,

                status="Secure",

                recommendation="Proceed with Key Exchange",

                color="green",

                secure=True,

            )

        elif self.secure_threshold < qber <= self.warning_threshold:

            return HealthReport(

                qber=qber,

                status="Warning",

                recommendation="Apply Privacy Amplification",

                color="orange",

                secure=True,

            )

        else:

            return HealthReport(

                qber=qber,

                status="Compromised",

                recommendation="Reject Key Exchange",

                color="red",

                secure=False,

            )

    @staticmethod
    def as_dictionary(report: HealthReport) -> dict:
        """
        Convert HealthReport into a dictionary.
        """

        return {

            "QBER (%)": round(report.qber, 2),

            "Status": report.status,

            "Recommendation": report.recommendation,

            "Color": report.color,

            "Secure": report.secure,

        }

    @staticmethod
    def status_icon(status: str) -> str:
        """
        Return a colored status icon.
        """

        icons = {

            "Secure": "🟢",

            "Warning": "🟡",

            "Compromised": "🔴",

        }

        return icons.get(status, "⚪")


def evaluate_channel(qber: float) -> dict:
    """
    Compatibility function used by protocol.py.

    Returns a dictionary containing the channel status.
    """

    monitor = QuantumCommunicationHealthMonitor()

    report = monitor.evaluate(qber)

    return monitor.as_dictionary(report)
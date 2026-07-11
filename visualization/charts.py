# Visualization helpers for charts
"""
QuantumSecureNet
----------------
Visualization Module

This module generates charts for the QuantumSecureNet dashboard.

Charts Included
---------------
1. QBER Comparison
2. Key Length Comparison
3. Basis Distribution
4. Error Distribution
5. QBER Gauge
6. Channel Status Card
"""

import matplotlib.pyplot as plt
import streamlit as st


class Charts:

    @staticmethod
    def plot_qber_comparison(normal_qber, noisy_qber, eve_qber):
        """
        Compare QBER for different scenarios.
        """

        scenarios = ["Normal", "Noisy", "Eve Attack"]
        values = [normal_qber, noisy_qber, eve_qber]

        fig, ax = plt.subplots(figsize=(6,4))

        bars = ax.bar(scenarios, values)

        ax.set_ylabel("QBER (%)")
        ax.set_title("QBER Comparison")

        for bar, value in zip(bars, values):
            ax.text(
                bar.get_x() + bar.get_width()/2,
                value + 0.5,
                f"{value:.2f}%",
                ha="center"
            )

        st.pyplot(fig)

    @staticmethod
    def plot_key_lengths(initial_length,
                         sifted_length,
                         final_length):

        labels = [
            "Initial Key",
            "Sifted Key",
            "Final Key"
        ]

        values = [
            initial_length,
            sifted_length,
            final_length
        ]

        fig, ax = plt.subplots(figsize=(6,4))

        bars = ax.bar(labels, values)

        ax.set_ylabel("Bits")
        ax.set_title("Key Length Comparison")

        for bar, value in zip(bars, values):

            ax.text(
                bar.get_x()+bar.get_width()/2,
                value+5,
                str(value),
                ha="center"
            )

        st.pyplot(fig)

    @staticmethod
    def plot_basis_distribution(matches,
                                discarded):

        labels = [
            "Matching Bases",
            "Discarded Bases"
        ]

        sizes = [
            matches,
            discarded
        ]

        fig, ax = plt.subplots(figsize=(5,5))

        ax.pie(
            sizes,
            labels=labels,
            autopct="%1.1f%%",
            startangle=90
        )

        ax.set_title("Basis Sifting Distribution")

        st.pyplot(fig)

    @staticmethod
    def plot_error_distribution(correct_bits,
                                error_bits):

        labels = [
            "Correct",
            "Errors"
        ]

        values = [
            correct_bits,
            error_bits
        ]

        fig, ax = plt.subplots(figsize=(5,4))

        bars = ax.bar(labels, values)

        ax.set_ylabel("Bits")

        ax.set_title("Error Distribution")

        for bar, value in zip(bars, values):

            ax.text(
                bar.get_x()+bar.get_width()/2,
                value+2,
                str(value),
                ha="center"
            )

        st.pyplot(fig)

    @staticmethod
    def plot_qber_gauge(qber):

        st.subheader("Current QBER")

        progress = min(qber / 25.0, 1.0)

        st.progress(progress)

        st.metric(
            "QBER",
            f"{qber:.2f}%"
        )

    @staticmethod
    def plot_status_card(status,
                         recommendation):

        if status == "Secure":

            st.success("🟢 Secure Channel")

        elif status == "Warning":

            st.warning("🟡 Warning")

        else:

            st.error("🔴 Compromised")

        st.info(f"Recommendation: {recommendation}")
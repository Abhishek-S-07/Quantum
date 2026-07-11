"""
===========================================================
QuantumSecureNet
Main Streamlit Dashboard

An Interactive BB84-Based Quantum Communication
and Security Analysis Platform

RIT Quant-A-Thon 2026

Part 1
-----------------------------------------------------------
• Imports
• Page Configuration
• Sidebar
• Session State
• Simulation Controls
• Execute BB84 Simulation
• Home Dashboard
===========================================================
"""

import streamlit as st
import pandas as pd

# ==========================================================
# BB84 Modules
# ==========================================================

from bb84.protocol import BB84Protocol

# ==========================================================
# Visualization Modules
# ==========================================================

from visualization.charts import Charts
from visualization.network import QuantumNetwork

# ==========================================================
# Streamlit Page Configuration
# ==========================================================

st.set_page_config(
    page_title="QuantumSecureNet",
    page_icon="🔐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================================
# Session State
# ==========================================================

if "results" not in st.session_state:
    st.session_state.results = None

# ==========================================================
# Title
# ==========================================================

st.title("🔐 QuantumSecureNet")

st.markdown(
"""
### An Interactive BB84-Based Quantum Communication and Security Analysis Platform

**Domain:** QT-4 – Quantum Communication

This dashboard demonstrates the complete lifecycle of the BB84
Quantum Key Distribution protocol including:

- Secure Key Generation
- Eve Attack Simulation
- Quantum Bit Error Rate (QBER)
- Error Reconciliation
- Privacy Amplification
- Quantum Communication Health Monitor (QCHM)
- Conceptual Multi-Node Network
"""
)

st.divider()

# ==========================================================
# Sidebar
# ==========================================================

st.sidebar.title("QuantumSecureNet")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🔑 BB84 Simulation",
        "📊 QBER Analysis",
        "🛡 Privacy Amplification",
        "🚦 QCHM",
        "🌐 Multi-Node Network",
        "📈 Statistics",
        "ℹ About"
    ]
)

st.sidebar.divider()

st.sidebar.subheader("Simulation Settings")

num_qubits = st.sidebar.slider(
    "Number of Qubits",
    min_value=100,
    max_value=5000,
    value=1000,
    step=100
)

noise_probability = st.sidebar.slider(
    "Noise Probability",
    min_value=0.0,
    max_value=0.30,
    value=0.02,
    step=0.01
)

eve_enabled = st.sidebar.checkbox(
    "Enable Eve Attack",
    value=False
)

run_simulation = st.sidebar.button(
    "▶ Run Simulation",
    use_container_width=True
)

st.sidebar.divider()

st.sidebar.success(
"""
Current Configuration

Protocol : BB84

Noise : {:.0f} %

Eve : {}

Qubits : {}
""".format(
noise_probability*100,
"Enabled" if eve_enabled else "Disabled",
num_qubits
)
)

# ==========================================================
# Execute Simulation
# ==========================================================

if run_simulation:

    with st.spinner("Executing BB84 Simulation..."):

        protocol = BB84Protocol(
            num_qubits=num_qubits,
            eve_enabled=eve_enabled,
            noise_probability=noise_probability
        )

        st.session_state.results = protocol.execute()

    st.success("Simulation Completed Successfully!")

# ==========================================================
# HOME PAGE
# ==========================================================

if page == "🏠 Home":

    st.header("Project Overview")

    st.write(
    """
QuantumSecureNet is an interactive educational platform
that demonstrates the complete BB84 Quantum Key Distribution
workflow.

Instead of implementing only the basic protocol,
our platform integrates every major stage of secure
quantum key exchange into a single dashboard.
"""
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Objectives")

        st.markdown(
        """
✅ Demonstrate BB84 Quantum Key Distribution

✅ Simulate Eve Intercept-Resend Attack

✅ Calculate Quantum Bit Error Rate

✅ Perform Error Reconciliation

✅ Apply Privacy Amplification

✅ Monitor Channel Health (QCHM)

✅ Visualize Conceptual Quantum Network
"""
        )

    with col2:

        st.subheader("Technology Stack")

        tech = pd.DataFrame({

            "Technology":[
                "Python",
                "Streamlit",
                "NumPy",
                "Matplotlib",
                "NetworkX",
                "SHA-256",
                "Qiskit (Concept)"
            ],

            "Purpose":[
                "Programming",
                "Dashboard",
                "Simulation",
                "Charts",
                "Network Visualization",
                "Privacy Amplification",
                "Quantum Computing"
            ]

        })

        st.dataframe(
            tech,
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    st.subheader("BB84 Workflow")

    st.markdown("""
1. Alice Generates Random Bits

2. Alice Chooses Random Bases

3. Quantum State Preparation

4. Quantum Transmission

5. Optional Eve Attack

6. Quantum Noise

7. Bob Measurement

8. Basis Reconciliation (Sifting)

9. QBER Calculation

10. Error Reconciliation

11. Privacy Amplification

12. Quantum Communication Health Monitor
""")

    st.info(
        "Use the sidebar to configure the simulation and click "
        "'Run Simulation' to generate results."
    )

# ==========================================================
# Remaining Pages
# (Implemented in Parts 2–4)
# ==========================================================

# ==========================================================
# BB84 SIMULATION
# ==========================================================

elif page == "🔑 BB84 Simulation":

    st.header("🔑 BB84 Quantum Key Distribution Simulation")

    if st.session_state.results is None:

        st.warning("Run the simulation from the sidebar first.")

    else:

        results = st.session_state.results

        st.success("Simulation Results")

        st.divider()

        ####################################################
        # Simulation Summary
        ####################################################

        col1, col2, col3, col4 = st.columns(4)

        with col1:
            st.metric(
                "Qubits",
                results["num_qubits"]
            )

        with col2:
            st.metric(
                "Sifted Key",
                results["sifted_key_length"]
            )

        with col3:
            st.metric(
                "Final Key",
                results["final_key_length"]
            )

        with col4:
            st.metric(
                "QBER",
                f'{results["qber"]:.2f}%'
            )

        st.divider()

        ####################################################
        # Alice & Bob
        ####################################################

        st.subheader("Alice and Bob")

        left, right = st.columns(2)

        with left:

            st.markdown("### Alice")

            st.write("Random Bits")

            st.code(
                "".join(map(str, results["alice_bits"][:64]))
            )

            st.write("Random Bases")

            st.code(
                "".join(map(str, results["alice_bases"][:64]))
            )

        with right:

            st.markdown("### Bob")

            st.write("Measured Bits")

            st.code(
                "".join(map(str, results["bob_bits"][:64]))
            )

            st.write("Measurement Bases")

            st.code(
                "".join(map(str, results["bob_bases"][:64]))
            )

        st.divider()

        ####################################################
        # Channel Configuration
        ####################################################

        st.subheader("Transmission Configuration")

        col1, col2 = st.columns(2)

        with col1:

            if results["eve_enabled"]:

                st.error("Intercept-Resend Attack Enabled")

            else:

                st.success("No Eavesdropping")

        with col2:

            st.info(
                f'Noise Probability : {results["noise_probability"]*100:.2f}%'
            )

        st.divider()

        ####################################################
        # Sifted Keys
        ####################################################

        st.subheader("Basis Reconciliation (Sifting)")

        st.write(
            "Only positions where Alice and Bob selected the same basis are retained."
        )

        col1, col2 = st.columns(2)

        with col1:

            st.markdown("### Alice Sifted Key")

            st.code(
                "".join(
                    map(
                        str,
                        results["sifted_alice_key"][:128]
                    )
                )
            )

        with col2:

            st.markdown("### Bob Sifted Key")

            st.code(
                "".join(
                    map(
                        str,
                        results["sifted_bob_key"][:128]
                    )
                )
            )

        st.divider()

        ####################################################
        # Corrected Key
        ####################################################

        st.subheader("Error Reconciliation")

        st.write(
            "Simplified parity-based reconciliation corrects mismatched bits."
        )

        st.code(
            "".join(
                map(
                    str,
                    results["sifted_key"][:128]
                )
            )
        )

        st.success(
            f'Corrected Key Length : {results["sifted_key_length"]} bits'
        )

        st.divider()

        ####################################################
        # Final Secure Key
        ####################################################

        st.subheader("Privacy Amplification")

        st.write(
            "SHA-256 is applied to compress the reconciled key into a secure final key."
        )

        st.code(
            "".join(
                map(
                    str,
                    results["final_key"][:256]
                )
            )
        )

        st.success(
            f'Final Secure Key Length : {results["final_key_length"]} bits'
        )

        st.divider()

        ####################################################
        # Status
        ####################################################

        st.subheader("Simulation Status")

        status = results["status"]

        if isinstance(status, dict):

            state = status.get("Status", "")

        else:

            state = getattr(status, "status", "")

        if state == "Secure":

            st.success("🟢 Secure Quantum Channel")

        elif state == "Warning":

            st.warning("🟡 Warning")

        else:

            st.error("🔴 Compromised")

        st.info(
            "Proceed to QBER Analysis for a detailed security evaluation."
        )

# ==========================================================
# QBER ANALYSIS
# ==========================================================

elif page == "📊 QBER Analysis":

    st.header("📊 Quantum Bit Error Rate (QBER) Analysis")

    if st.session_state.results is None:

        st.warning("Run a BB84 simulation first.")

    else:

        results = st.session_state.results

        qber = results["qber"]

        sifted_length = results["sifted_key_length"]

        final_length = results["final_key_length"]

        initial_length = results["num_qubits"]

        error_bits = round((qber / 100) * sifted_length)

        correct_bits = sifted_length - error_bits

        ####################################################

        st.subheader("Current QBER")

        Charts.plot_qber_gauge(qber)

        st.divider()

        ####################################################

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "QBER",
                f"{qber:.2f}%"
            )

        with col2:
            st.metric(
                "Sifted Key",
                sifted_length
            )

        with col3:
            st.metric(
                "Estimated Errors",
                error_bits
            )

        st.divider()

        ####################################################
        # Key Length Chart
        ####################################################

        st.subheader("Key Length Comparison")

        Charts.plot_key_lengths(

            initial_length,

            sifted_length,

            final_length

        )

        st.divider()

        ####################################################
        # Basis Distribution
        ####################################################

        matches = sifted_length

        discarded = initial_length - sifted_length

        st.subheader("Basis Sifting")

        Charts.plot_basis_distribution(

            matches,

            discarded

        )

        st.divider()

        ####################################################
        # Error Distribution
        ####################################################

        st.subheader("Error Distribution")

        Charts.plot_error_distribution(

            correct_bits,

            error_bits

        )

        st.divider()

        ####################################################
        # Demo Comparison
        ####################################################

        st.subheader("Scenario Comparison")

        Charts.plot_qber_comparison(

            normal_qber=1.2,

            noisy_qber=6.8,

            eve_qber=max(18.0, qber)

        )

        st.info(
            "Normal and Noisy values are reference values for comparison. "
            "The current simulation QBER is shown above."
        )

# ==========================================================
# PRIVACY AMPLIFICATION
# ==========================================================

elif page == "🛡 Privacy Amplification":

    st.header("🛡 Privacy Amplification")

    if st.session_state.results is None:

        st.warning("Run a BB84 simulation first.")

    else:

        results = st.session_state.results

        st.subheader("Purpose")

        st.write(
            """
Privacy amplification removes any partial information that an
eavesdropper may possess after reconciliation.

QuantumSecureNet demonstrates this using SHA-256 hashing.
"""
        )

        st.divider()

        ####################################################

        col1, col2 = st.columns(2)

        with col1:

            st.metric(

                "Reconciled Key Length",

                results["sifted_key_length"]

            )

        with col2:

            st.metric(

                "Final Secure Key Length",

                results["final_key_length"]

            )

        st.divider()

        ####################################################

        st.subheader("Reconciled Key")

        st.code(

            "".join(

                map(

                    str,

                    results["sifted_key"][:256]

                )

            )

        )

        st.subheader("Final Secure Key")

        st.code(

            "".join(

                map(

                    str,

                    results["final_key"][:256]

                )

            )

        )

        st.divider()

        reduction = (

            results["sifted_key_length"]

            -

            results["final_key_length"]

        )

        compression = 0.0

        if results["sifted_key_length"] > 0:

            compression = (

                reduction

                /

                results["sifted_key_length"]

            ) * 100

        st.metric(

            "Compression",

            f"{compression:.2f}%"

        )

        st.success(

            "SHA-256 successfully generated the final secure key."

        )

# ==========================================================
# QCHM
# ==========================================================

elif page == "🚦 QCHM":

    st.header("🚦 Quantum Communication Health Monitor")

    if st.session_state.results is None:

        st.warning("Run a BB84 simulation first.")

    else:

        results = st.session_state.results

        report = results["status"]

        ####################################################

        if hasattr(report, "status"):

            status = report.status

            recommendation = report.recommendation

            qber = report.qber

        else:

            status = report["Status"]

            recommendation = report["Recommendation"]

            qber = report["QBER (%)"]

        ####################################################

        Charts.plot_status_card(

            status,

            recommendation

        )

        st.divider()

        ####################################################

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(

                "QBER",

                f"{qber:.2f}%"

            )

        with col2:

            st.metric(

                "Status",

                status

            )

        with col3:

            st.metric(

                "Recommendation",

                recommendation

            )

        st.divider()

        ####################################################

        st.subheader("Security Interpretation")

        if status == "Secure":

            st.success(

                """
QBER is below the secure threshold.

The communication channel is considered secure
and key exchange can proceed.
"""
            )

        elif status == "Warning":

            st.warning(

                """
Moderate QBER detected.

Privacy amplification is recommended before
using the generated key.
"""
            )

        else:

            st.error(

                """
High QBER detected.

The communication channel is considered
compromised.

Reject this key exchange.
"""
            )

# ==========================================================
# MULTI-NODE NETWORK
# ==========================================================

elif page == "🌐 Multi-Node Network":

    st.header("🌐 Conceptual Multi-Node Quantum Network")

    st.write(
        """
This visualization represents a conceptual quantum communication
network.

Alice securely exchanges quantum keys with Bob through trusted
relay nodes. Eve represents a potential eavesdropper attempting
to intercept the quantum channel.
"""
    )

    network = QuantumNetwork()

    fig = network.draw_network()

    st.pyplot(fig)

    st.divider()

    st.subheader("Network Components")

    network_data = pd.DataFrame({

        "Node":[
            "Alice",
            "Relay-1",
            "Relay-2",
            "Bob",
            "Eve"
        ],

        "Role":[
            "Sender",
            "Trusted Relay",
            "Trusted Relay",
            "Receiver",
            "Eavesdropper"
        ]

    })

    st.dataframe(
        network_data,
        hide_index=True,
        use_container_width=True
    )

    st.info(
        "This network is a conceptual visualization for educational purposes."
    )

# ==========================================================
# SIMULATION STATISTICS
# ==========================================================

elif page == "📈 Statistics":

    st.header("📈 Simulation Statistics")

    if st.session_state.results is None:

        st.warning(
            "Run the simulation first."
        )

    else:

        results = st.session_state.results

        st.subheader("Simulation Summary")

        summary = pd.DataFrame({

            "Parameter":[

                "Number of Qubits",

                "Noise Probability",

                "Eve Enabled",

                "Sifted Key Length",

                "Final Key Length",

                "QBER (%)"

            ],

            "Value":[

                results["num_qubits"],

                f'{results["noise_probability"]*100:.2f}%',

                "Yes" if results["eve_enabled"] else "No",

                results["sifted_key_length"],

                results["final_key_length"],

                f'{results["qber"]:.2f}%'

            ]

        })

        st.dataframe(

            summary,

            hide_index=True,

            use_container_width=True

        )

        st.divider()

        ###################################################

        st.subheader("Performance Metrics")

        c1, c2, c3 = st.columns(3)

        with c1:

            efficiency = (
                results["sifted_key_length"]
                /
                results["num_qubits"]
            ) * 100

            st.metric(

                "Sifting Efficiency",

                f"{efficiency:.2f}%"

            )

        with c2:

            compression = (
                (
                    results["sifted_key_length"]
                    -
                    results["final_key_length"]
                )
                /
                max(results["sifted_key_length"],1)
            ) * 100

            st.metric(

                "Compression",

                f"{compression:.2f}%"

            )

        with c3:

            if results["qber"] <= 5:

                security = "High"

            elif results["qber"] <= 11:

                security = "Medium"

            else:

                security = "Low"

            st.metric(

                "Security Level",

                security

            )

        st.divider()

        ###################################################

        st.subheader("Protocol Workflow")

        workflow = [

            "Alice Generated Random Bits",

            "Alice Selected Random Bases",

            "Quantum States Prepared",

            "Transmission Completed",

            "Optional Eve Attack",

            "Quantum Noise Applied",

            "Bob Measured Qubits",

            "Basis Reconciliation",

            "QBER Calculation",

            "Error Reconciliation",

            "Privacy Amplification",

            "QCHM Evaluation"

        ]

        for step in workflow:

            st.success(step)

# ==========================================================
# ABOUT
# ==========================================================

elif page == "ℹ About":

    st.header("ℹ About QuantumSecureNet")

    st.write(
        """
QuantumSecureNet is an educational platform demonstrating
the BB84 Quantum Key Distribution protocol through
interactive simulation and visualization.
"""
    )

    st.divider()

    st.subheader("Core Features")

    features = [

        "BB84 Quantum Key Distribution",

        "Random Bit Generation",

        "Quantum State Preparation",

        "Basis Reconciliation",

        "Quantum Noise Simulation",

        "Intercept-Resend Eve Attack",

        "Quantum Bit Error Rate (QBER)",

        "Simplified Error Reconciliation",

        "Privacy Amplification using SHA-256",

        "Quantum Communication Health Monitor",

        "Conceptual Multi-Node Network",

        "Interactive Streamlit Dashboard"

    ]

    for feature in features:

        st.markdown(f"✅ {feature}")

    st.divider()

    st.subheader("Technology Stack")

    tech = pd.DataFrame({

        "Technology":[

            "Python",

            "Streamlit",

            "NumPy",

            "Matplotlib",

            "NetworkX",

            "Hashlib (SHA-256)",

            "Qiskit (Conceptual Integration)"

        ],

        "Purpose":[

            "Programming Language",

            "Interactive Dashboard",

            "Scientific Computing",

            "Graphs & Charts",

            "Network Visualization",

            "Privacy Amplification",

            "Quantum Computing Framework"

        ]

    })

    st.dataframe(

        tech,

        hide_index=True,

        use_container_width=True

    )

    st.divider()

    st.success(
        """
QuantumSecureNet

An Interactive BB84-Based Quantum Communication
and Security Analysis Platform

Developed for

RIT Quant-A-Thon 2026

Domain:
QT-4 Quantum Communication

Problem Statement:
QT-4.2
"""
    )



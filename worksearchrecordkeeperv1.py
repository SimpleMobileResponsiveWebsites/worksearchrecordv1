import streamlit as st
import pandas as pd
from datetime import date


def main():
    st.title("Work Search Record")
    st.write("Keep a detailed record of your work search activities for each week that you request benefits.")

    # Specific Contacts/Job Applications
    st.header("Specific Contacts/Job Applications")

    contacts_df = pd.DataFrame(columns=[
        "Date of Contact",
        "Company Name & Address",
        "Phone/Fax Number",
        "Person Contacted",
        "Position Applied For",
        "Method of Contact",
        "Results"
    ])

    num_entries = st.number_input("Number of job application entries", min_value=1, max_value=10, value=5)

    for i in range(num_entries):
        st.subheader(f"Entry {i + 1}")

        date_contact = st.date_input("Date of Contact", key=f"date_{i}")
        company = st.text_input("Company Name & Address", key=f"company_{i}")
        phone = st.text_input("Phone/Fax Number", key=f"phone_{i}")
        person = st.text_input("Person Contacted", key=f"person_{i}")
        position = st.text_input("Position Applied For", key=f"position_{i}")
        method = st.selectbox("Method of Contact", ["Phone", "Resume", "Application", "In-Person"], key=f"method_{i}")
        results = st.text_input("Results", key=f"results_{i}")

        if company:  # Only add non-empty entries
            contacts_df = contacts_df.append({
                "Date of Contact": date_contact,
                "Company Name & Address": company,
                "Phone/Fax Number": phone,
                "Person Contacted": person,
                "Position Applied For": position,
                "Method of Contact": method,
                "Results": results
            }, ignore_index=True)

    if not contacts_df.empty:
        st.subheader("Recorded Contacts/Applications")
        st.dataframe(contacts_df)

    # Other Work Search Activities
    st.header("Other Work Search Activities")
    st.write("Job clubs, workshops, online & newspaper searches, etc.")

    activities_df = pd.DataFrame(columns=["Date of Activity", "Type of Activity"])

    num_activities = st.number_input("Number of other work search activities", min_value=1, max_value=5, value=3)

    for i in range(num_activities):
        st.subheader(f"Activity {i + 1}")
        date_activity = st.date_input("Date of Activity", key=f"act_date_{i}")
        activity_type = st.text_input("Type of Activity", key=f"act_type_{i}")

        if activity_type:  # Only add non-empty entries
            activities_df = activities_df.append({
                "Date of Activity": date_activity,
                "Type of Activity": activity_type
            }, ignore_index=True)

    if not activities_df.empty:
        st.subheader("Recorded Other Activities")
        st.dataframe(activities_df)

    # Save to CSV
    if st.button("Save Work Search Record"):
        full_df = pd.concat([contacts_df, activities_df], axis=0, ignore_index=True)
        csv = full_df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name=f"work_search_record_{date.today()}.csv",
            mime="text/csv"
        )


if __name__ == "__main__":
    main()

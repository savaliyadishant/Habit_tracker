import streamlit as st
import calendar

def main():
    # Set up your Streamlit app
    st.title("Calendar Display App")

    # Get the current year and month
    current_year = st.sidebar.slider("Select Year", 2000, 2050, 2024)
    current_month = st.sidebar.selectbox("Select Month", range(1, 13))

    # Create a calendar instance for the selected year and month
    cal = calendar.monthcalendar(current_year, current_month)

    # Display the calendar
    st.write(f"## Calendar for {calendar.month_name[current_month]} {current_year}")
    for week in cal:
        week_str = ' '.join([str(day) if day != 0 else '' for day in week])
        st.write(week_str)

if __name__ == "__main__":
    main()

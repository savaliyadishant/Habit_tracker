import streamlit as st
import datetime
import calendar

def display_calendar(year, month):
    # Create a calendar instance for the selected year and month
    cal = calendar.monthcalendar(year, month)

    # Display the calendar
    st.write(f"## Calendar for {calendar.month_name[month]} {year}")
    st.write("```\n")
    for week in cal:
        week_str = ' '.join([f"{day:2}" if day != 0 else '  ' for day in week])
        st.write(week_str)
    st.write("```")

def main():
    # Set up your Streamlit app
    st.title("Calendar Display App")

    # Get the current date
    current_date = datetime.datetime.now()

    # Get the current year and month
    current_year, current_month = current_date.year, current_date.month

    # Display the calendar for the current year and month
    display_calendar(current_year, current_month)

    # Option to navigate to the next or previous month
    st.sidebar.write("## Navigation")
    if st.sidebar.button("Previous Month"):
        if current_month == 1:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1
    if st.sidebar.button("Next Month"):
        if current_month == 12:
            current_month = 1
            current_year += 1
        else:
            current_month += 1

    # Update session state
    st.session_state.selected_year = current_year
    st.session_state.selected_month = current_month

if __name__ == "__main__":
    main()

import streamlit as st
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

    # Get the current year and month
    current_date = st.date_input("Select Date", value=None, min_value=None, max_value=None, key=None)

    # If date is not selected, display current month
    if not current_date:
        current_year, current_month, _ = st.date_input(label="", value=None, min_value=None, max_value=None, key=None, help="Select Date")
        if not current_year or not current_month:
            current_year, current_month = st.session_state.selected_year, st.session_state.selected_month
        else:
            st.session_state.selected_year = current_year
            st.session_state.selected_month = current_month
    else:
        current_year, current_month, _ = current_date.year, current_date.month, current_date.day

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

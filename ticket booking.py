import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mysql_config = {
    'host': 'localhost',
    'database': 'ticket_booking',
    'user': 'root',
    'password': '12345'
}
def book_ticket():
    print("Welcome to Movie Ticket Booking System")
    print("Available Movies: Conjuring, Run, Evil Dead, Spiderman")
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    movie = input("Enter the movie you want to watch: ")
    try:
        conn = mysql.connector.connect(**mysql_config)
        cursor = conn.cursor()
        insert_query = "INSERT INTO bookings (name, email, movie) VALUES (%s, %s, %s)"
        cursor.execute(insert_query, (name, email, movie))
        conn.commit()
        cursor.close()
        conn.close()
        send_email(name, email, movie)
        generate_booking_file(name, email, movie)
        print("Booking successful! Check your email for confirmation.")
    except mysql.connector.Error as err:
      print(f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            conn.close()
def send_email(name, email, movie):
    from_email = 'dineshdinesh112004@gmail.com'  
    to_email = email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = 'Movie Ticket Booking Confirmation'
    body = f"Hello {name},\n\nYou have successfully booked tickets for the movie: {movie}.\n\nEnjoy the show!\n\nRegards,\nMovie Ticket Booking Team"
    msg.attach(MIMEText(body, 'plain'))
    smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_server.starttls()
    smtp_server.login(from_email, 'bihg dyyw vbmh gmwl') 
    text = msg.as_string()
    smtp_server.sendmail(from_email, to_email, text)
    smtp_server.quit()
def generate_booking_file(name, email, movie):
    filename = f"{name}_booking_details.txt"
    with open(filename, 'w') as file:
        file.write(f"Booking Details\n\nName: {name}\nEmail: {email}\nMovie: {movie}\n")
if __name__ == "__main__":
    book_ticket()



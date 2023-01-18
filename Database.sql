

insert into customer(id, full_name, tickets)
values (
1, "Kezia", 5
); 
insert into event_booking(booking_id, event_id, venue_id, date_start, date_end)
values (
1, 1, 1, 20, 25
);

insert into events(id, event_name, organizer_id, start_time, end_time, venues, total_capacity, total_sales)
values (
1, 'flash', 'o1', 1500, 1800, 5, 1000, 300 
);
insert into organizer(id, name)
values (
1, 'wassup'
);
insert into ticket_order(id, event_id, venue_id, ticket_price, tickets_ordered, order_date, total_price)
values(
1, 1, 1, 20, 5, 10, 200
);
insert into venues(venue_id, location, max_capacity, booked)
values(
1, 'jakarta', 1000, True
);
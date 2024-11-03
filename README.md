# Wolt-Reverse-Engineering-Assignment
A Python script is being developed to replicate the  identified API calls, which handles authentication tokens  and sends requests to the captured endpoints.
Assignment: Reverse Engineering any
 Application to Analyze Its Requests and
 Replicate Them
 Objective: Evaluate reverse engineering skills by analyzing applications to
 identify activities, advanced authentication mechanisms, and replicate API
 calls.
 1. Application Selection
 Chosen Application: Wolt App (Mobile Application)
 Wolt is a food delivery service that enables users to order
 from local restaurants through its mobile app, offering features
 like real-time order tracking and in-app messaging for
 customer support

 2. Reverse Engineering Tasks
 A. Analyze the Activity Process
 ● User Activities:
 ○ Login: Users can log in using email, Facebook, Google, or
 as a guest while selecting the location manually or
 automatically.
 ○ Browsing restaurants
 ○ Adding items to the cart
○ Checking out
 ○ Sending messages via the in-app messenge
 ● Communication with Backend:
 ○ Theapplication communicates with its backend through
 various API calls during user activities, such as searching
 for venues, checking out, and messaging.

 B. Identify API Endpoints and Authentication Mechanisms
 ● Tools Used:
 ○ Burp Suite for capturing API calls
 ● Captured API Endpoints:
 ○ GetVenue Information
 ■ GET
 /order-xp/mobile/v1/pages/venue?venue_i
 d={venue_id}&lat={lat}&lon={lon}
 ○ Search Restaurants
 ■ POST /v1/pages/search
 ○ Checkout Process
 ■ POST /order-xp/v1/pages/checkout
 ○ Consumer Registration
 ■ POST /v1/consumer
 ○ Messenger Conversation Reply
 ■ POST
 /messenger/mobile/conversations/{conver
 sation_id}/reply
 ○ Messenger Home
 ■ POST /messenger/mobile/home
● Authentication Mechanisms:
 ○ Cookies and Tokens:
 ■ Theapplication uses session IDs
 (w-wolt-session-id) and visitor IDs
 (x-wolt-visitor-id) for maintaining user
 sessions.
 ○ Authorization:
 ■ Basic authentication is used for some endpoints, as
 seen in the messenger API.
 
 C. Mobile Application Analysis
 ● Tools Used:
 ○ Frida for dynamic analysis
 ○ Genymotion for setting up an Android pentesting lab
 ● Findings:
 ○ Identified functions related to API calls and user session
 management.
○ Observed the generation and usage of session tokens.
 ○ UsedFrida to bypass SSL pinning during the analysis.
 
 D. Replicate the API Calls
 ● Python Script:
 ○ APython script is being developed to replicate the
 identified API calls, which handles authentication tokens
 and sends requests to the captured endpoints.

 4. Use of Advanced Tools
 ● Tools Demonstrated:
 ○ BurpSuite: For intercepting and analyzing requests.
 ○ Frida: For dynamic instrumentation and analysis of mobile
 applications.
 
 5. Challenges Faced
 ● Capturing API Calls:
 Issue: The Wolt app implemented various security measures
 that made it challenging to intercept certain API calls during user
 activities. The use of HTTPS and other protective mechanisms
 hindered the ability to monitor requests effectively.
 ● Bypassing Security Mechanisms:
 Issue: Some API calls were secured with SSL pinning, which
 prevents unauthorized access and interception of the
 communication between the app and the server. This security
 feature complicates the analysis by making it difficult to capture
 and analyze network traffic.
 ● Complex Authentication Process:
 Issue: The app utilized dynamic tokens and session
 management techniques, making it necessary to understand the
 lifecycle of these tokens and how they were generated and
 refreshed.
 ● Solutions:
 Utilization of Frida: Employed Frida for dynamic analysis, which
 allowed for the instrumentation of the app in real-time, used
 Objection. This approach enabled the bypassing of SSL pinning,
 granting access to network traffic and allowing for the capture of
 the necessary API calls.
 Monitoring Network Traffic: Used Burp Suite in conjunction
 with Frida to monitor and log network traffic effectively. This
 combination provided insights into the API endpoints being
 called and the parameters being sent.
 Analyzing Code: Conducted a thorough analysis of the app’s
 code using Frida to identify how tokens were generated and
 managed, facilitating the understanding of the authentication
 process.

7. Screenshots Of Tasks!
   [Screenshot 2024-11-02 050731](https://github.com/user-attachments/assets/ded0d807-4075-4750-905e-057edb221b42)
   ![Screenshot 2024-11-02 050747](https://github.com/user-attachments/assets/25d9f092-cce3-49f1-bba2-7199140ae1ab)
   ![Screenshot 2024-11-02 050303](https://github.com/user-attachments/assets/eef5d7b8-6ea1-4328-8a50-33e0c9f4329e)
   ![Screenshot 2024-11-02 201101](https://github.com/user-attachments/assets/2518c10e-3179-45c6-aa27-e69da7beb35c)


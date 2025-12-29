**User Story**

As a **campaign manager**

I want **to understand the response rate of my campaign**

So that **see if the progress is good or I should adjust my campaign**

**LinkAcceptance Criteria**

**Scenario 1:**
**Given** an Infinity campaign (NOT a Finder campaign) in state Published or Retired
**When** I come to the campaign overview screen
**Then** I see at the top instead of the number of answers:

1. A top banner with top metrics:
   1. Response rate - **response\_rate**
   2. Number of users who viewed the campaign (! use the standard formatter for numbers) - **viewed**
2. A top section with 3 parts:
   1. A first widget, 3-value gauge, showing:
      1. Center = number of targeted - **targeted** 
      2. Green = number of responses in state answered - **answered**
      3. Yellow = number of pending responses - **pending**
      4. Red = number of responses in state declined - **declined**
   2. A bar chart, fixed timeframe of 30 days, showing number of answers and declines per day
   3. A right column with:
      1. Basic information retrieved from the campaign definition in BCS:
         1. Campaign status - Published, Retired
         2. Last published date - if empty, then "-"
         3. Priority - Normal, Urgent
         4. Trigger - Name of the trigger as displayed in the screen - Manual, API, Schedule
      2. Breakdown by more detailed information - see below query for the way to compute and get the values
         1. Answered fully - ANSWERED/fully
         2. Answered partially - ANSWERED/partially
         3. Pending display - PLANNED/empty or TARGET/offline
         4. Notified - TARGETED/notified
         5. Opened - TARGETED/opened
         6. Postponed - TARGETED/postponed
         7. Declined - DECLINED/empty
         8. Expired - CANCELED/expired
   4. A kebab menu at the top with on entry "Investigate all campaign responses" that opens an investigation with the same NQL query as available today behind "Investigate all"

Data for (1), (2.1) and (2.3) can be retrieved via a single NQL query (better for performance - in case we have to split, you can remove from the summarize part the not needed fields):

campaign.responses
\| where campaign.nql\_id == "#the\_nql\_id"
\| summarize targeted = countif(state != canceled or state\_details == expired), viewed = countif(historical\_state\_details contains "notified" or state in \[answered, declined]), response\_rate = countif(state == answered) / countif(state != canceled or state\_details == expired), answered = countif(state == answered), pending = countif(state in \[targeted, planned]), declined = countif(state == declined), Answered\_partially = countif( state\_details == partially ), Postponed = countif( state\_details == postponed ), Expired = countif( state\_details == expired )&#x20;

The percentages version for (2.3) can be computed based on the absolute numbers, divided by total "targeted"

Data for (2.2) can be retrieved with a single NQL query compatible with WaaS out-of-the-box:

campaign.responses past 30d
\| where campaign.nql\_id == "#the\_nql\_id" and state in \[answered, declined]
\| summarize Answers\_ = countif(state == answered), Declines\_ = countif(state == declined) by 1d&#x20;
# IOS14 Update Report

> Part of the [[00 - Secret Sauce Index|Secret Sauce]] course. See also [[Sales MOC]] · [[Marketing MOC]].

The iOS14 update requires APPS to use the AppTrackingTransparency (ATT) Framework.

- Request user authorization to access app-related data. Permission must be granted to track the users actions
- This is to protect the privacy of the user

## As per Facebook regarding this update

- Apple is trying to stop users being tracking by other apps like FB, IG, Google, YT
- This update is not about privacy but about profit
- Small business are going to suffer the most since this affects the machine learning of Facebook's Algorithm

## What happens if a user opts out of tracking?

- Less personalized ads to user = **Poorly targeted ads**
- Less Personal Facebook Newsfeed = **Poorly recommended organic content**
- In-app activity won't be tracked = **Will hit placements badly like audience network**

## What are the changes so far?

- **Attribution Setting Column**
  - Default attribution window is **7-day click and 1-day view**
    - If you don't change the previous campaigns conversion window into this default attribution window then there will be some data that won't be seen at the campaign level
    - Optimization Impact of this attribution window:
      - **Negatively impact** ad set optimization (learning) for not having as much data as before
      - **Custom audience size will drop** (including existing audiences who opted out of tracking)
      - Loss of demographic breakdown
  - 28-day view; 7-day view; 28-days click attribution windows will no longer be available

- **8 Conversions Limit**
  - 8 unique conversion events per website domain
    - eCommerce won't be greatly affected unless they use custom conversion
  - Ad sets optimizing for a conversion event that's no longer available will be paused
  - If a user opts out of tracking on iOS14, you will only be able to the last conversion event that they have completed
    - I.e. for eCommerce:
      - If an Apple user who opted out of the tracking click on your ad and the last action they did was Added an Item to Cart, then FB will only track ATC event. The previous event won't be tracked (View Content, Page View)

## What to do now?

- **Attribution Setting**
  - Columns of old campaigns are not reflecting correct data:
    - Activating and deactivating affected campaigns
    - Or Change the conversion window to the new default setting
  - Total columns is not adding up
    - Filter and separate campaigns according to the attribution window

- **Adapt to 8 - Conversion Events**
  - Facebook will initially automatically choose the 8 events
  - We can now rank these events base on which is the most valuable to our business

- **Verify your domain**
  - https://developers.facebook.com/docs/sharing/domain-verification/
  - If you want to have control over the 8 conversion events, your website must be verified
  - This will also keep your account safe + business verification
  - **Business Verification**
    - If it's not business verified, you are more prone to getting your ad account restricted
      - Once restricted, you could not appeal it if the business is not verified

- **Prepare for inaccurate data report**
  - No longer rely on the data you see in ads manager
  - Recommendation: Track you data using other platforms like google analytics

- **Find other sources of traffic**
  - Time to be active in other social media platforms to generate more traffic: Google, Youtube, Tiktok, LinkedIn

- **Improve Your Sales Funnel**
  - Leverage on email lead generation & Build an email list
  - Increase customer lifetime value (CLTV); Good after sales service, bonuses for referral & increase loyal audience

---
Source: Secret Sauce/17th - iOS14 Update Report.pdf

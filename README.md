# LifeTracker
## Technical Documentation

[The wiki](https://github.com/SeanGrady/life_tracker/wiki)

## Why a life tracker?
### Patterns
We are not always adept at recognizing cause/effect patterns that influence our lives. Some of these patterns take place over too long of a time period to be easily noticed. For example, daily vitamin D supplementation can take 2-3 months to noticeably affect mood in the best of cases, and up to a year to completely reverse severe deficiency. Other patterns occur over short timescales but still have too much lag between the cause and the effect to be easily noticed, especially if the link between the two doesn't seem obvious--like the mild "hangover" affect some people get the day _after_ eating too much sugar. Still other patterns affect "noisy" aspects of our lives which many other factors influence. Folks with mood disorders are very familiar with this category: I feel a lot better today, it must be the new morning exercise routine! Or... is it the caffeine I had before lunch? Or that I got more sleep than usual last night? Maybe it was the ibuprofen I took yesterday, I've heard that can have an impact on mood...

The best way to begin addressing these kinds of disconnects is with data. It's a lot easier to notice that you always feel awful the day after you eat too much salt if you can graph your salt intake and daily well-being side by side. There are many different existing solutions that try to solve all or part of this issue, but I have found none that provide all of the three things that are, in my opinion, essential to success:

* **Centralization**: an easy way to get all your data in one place. Food, exercise, sleep, whatever else you happen to be tracking.

* **Personalization**: an easy way to define and track any personal metric that you want to improve. Weight is one example that's pretty well handled by existing solutions, but what about energy levels? Or flexibility? Or chronic symptoms?

* **Pattern Recognition**: an easy way to find correlations and cause/effect relationships in the data. In the simplest case just being able to look at your data side-by-side can reveal surprising things.

### Logging for Humans
We are not always good at answering questions about ourselves and our past behavior, which makes it hard to know if something you're trying to change is actually improving or worsening without being able to go back and look at past data.  I track my food consumption meticulously, but if you were to ask me to tell you how many calories I ate per day this week without checking first I would be very confident and probably very wrong.

In a perfect world, you would put all your data into this app and it would immediately pop up a helpful assistant with a dialogue box that said something like "It looks like you're trying to get rid of chronic headaches. You've been skipping lunch a lot, have you tried eating more frequently during the day?" While this is a wonderful long-term goal, it's certainly beyond the scope of a personal project done in one's spare time. We're smart critters, though, and usually we have a pretty good idea of what we might want to change. The hope behind this project is that an easy, customizable, and reliable means of tracking actions and target metrics is enough to help people more effectively help themselves.

## What this project aims to do

* Integrate with as many existing data collection and tracking solutions as possible. Examples are food tracking apps (like LoseIt, MyFitnessPal and Cronometer), or exercise tracking devices (like Fitbit or the Apple Watch).
* Provide a flexible interface for defining your own metrics and logging them. Tags that can be applied to any given day (for example, `headache` if you had a headache that day) are one possible method. Custom survey questions emailed to you every evening asking questions about your day ("On a scale of 1 to 5 how severe was your anxiety today?") are another.
* Make it easy to compare any and all of your data to discover trends over time as well as correlations or cause/effect relationships.
* Allow other people (e.g. personal trainers, primary care doctors, family members) access to some or all of your data.

## What this project does not aim to do

* Any kind of machine learning or data analysis. This is something I would like to explore as I continue to flesh out the project, but the reality is that aside from some very basic statistical analysis there will almost certainly not be enough data to learn anything meaningful with these methods.
* Be anywhere near anything HIPAA-related. Currently, the HIPAA regulations say that broadly speaking as long as you don't bill health insurance or work with anyone who does, you are not a covered entity. Therefore, while providing the information in this app to anyone of your choice including your healthcare provider(s) should be easy for a user to do, working with anyone who is a HIPAA-covered entity or business associate is right out.

## What this project may aim to do in the future

* Integrate data that was originally HIPAA-covered PHI, such as lab results obtained with your primary care physician--think tracking cholesterol levels over time. I am not a HIPAA lawyer, but my understanding of the regulations is that if a user independently requests their medical data from their healthcare provider(s) and voluntarily uploads it to an app like this one, it is no longer covered under HIPAA. I will want to consult someone who _is_ a HIPAA lawyer before starting anything like this.
* Implement limited machine learning. Bag-of-words sentiment analysis on uploaded journal entries is one possible example of a method that may yield useful results, since it can use existing models and does not need to be trained directly on user data, of which there will be relatively little.

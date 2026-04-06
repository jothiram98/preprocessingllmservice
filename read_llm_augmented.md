Work Stream XYZ

Version # 1.0

Last Revised Date

## Process Implementation Date

SOP Owner

SOP Approver

## Table of Contents

|   1. | Overview .........................................................................................................................................2    | Overview .........................................................................................................................................2    | Overview .........................................................................................................................................2    |
|------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
|      | 1.1 General Information ..............................................................................................................2                | 1.1 General Information ..............................................................................................................2                | 1.1 General Information ..............................................................................................................2                |
|      | 1.2 Related Internal Policies and Processes ..............................................................................2                            | 1.2 Related Internal Policies and Processes ..............................................................................2                            | 1.2 Related Internal Policies and Processes ..............................................................................2                            |
|      | 1.3 Systems/Tools ......................................................................................................................2              | 1.3 Systems/Tools ......................................................................................................................2              | 1.3 Systems/Tools ......................................................................................................................2              |
|      | 1.3.1 Global Systems/Tools .................................................................................................2                          | 1.3.1 Global Systems/Tools .................................................................................................2                          | 1.3.1 Global Systems/Tools .................................................................................................2                          |
|      | 1.3.2 Market-specific/Regional Systems/Tools ................................................................2                                         | 1.3.2 Market-specific/Regional Systems/Tools ................................................................2                                         | 1.3.2 Market-specific/Regional Systems/Tools ................................................................2                                         |
|    2 | Executive Summary ......................................................................................................................3              | Executive Summary ......................................................................................................................3              | Executive Summary ......................................................................................................................3              |
|      | 2.1 Synopsis................................................................................................................................3          | 2.1 Synopsis................................................................................................................................3          | 2.1 Synopsis................................................................................................................................3          |
|      | 2.2 Objective ...............................................................................................................................5         | 2.2 Objective ...............................................................................................................................5         | 2.2 Objective ...............................................................................................................................5         |
|      | 2.3 Process-specific Service Level Agreements (SLAs) ............................................................5                                     | 2.3 Process-specific Service Level Agreements (SLAs) ............................................................5                                     | 2.3 Process-specific Service Level Agreements (SLAs) ............................................................5                                     |
|      | 2.4 Risks and Controls................................................................................................................5                | 2.4 Risks and Controls................................................................................................................5                | 2.4 Risks and Controls................................................................................................................5                |
|      | 2.4.1 Global Risks and Controls ..........................................................................................5                            | 2.4.1 Global Risks and Controls ..........................................................................................5                            | 2.4.1 Global Risks and Controls ..........................................................................................5                            |
|      | 2.4.2 Market-Specific Risks and Controls .........................................................................5                                    | 2.4.2 Market-Specific Risks and Controls .........................................................................5                                    | 2.4.2 Market-Specific Risks and Controls .........................................................................5                                    |
|      | 2.5 Roles and Responsibilities....................................................................................................5                    | 2.5 Roles and Responsibilities....................................................................................................5                    | 2.5 Roles and Responsibilities....................................................................................................5                    |
|    3 | Inputs ..............................................................................................................................................6 | Inputs ..............................................................................................................................................6 | Inputs ..............................................................................................................................................6 |
|    4 | Process Map ...................................................................................................................................7       | Process Map ...................................................................................................................................7       | Process Map ...................................................................................................................................7       |
|      | Process Description .......................................................................................................................8           | Process Description .......................................................................................................................8           | Process Description .......................................................................................................................8           |
|    5 | Submit the Request to Update a Country Code                                                                                                            | Submit the Request to Update a Country Code                                                                                                            | Submit the Request to Update a Country Code                                                                                                            |
|      | 5.1 ...................................................................8                                                                               | 5.1 ...................................................................8                                                                               | 5.1 ...................................................................8                                                                               |
|      | 5.3 Obtain Requisite Approval ..................................................................................................24                     | 5.3 Obtain Requisite Approval ..................................................................................................24                     | 5.3 Obtain Requisite Approval ..................................................................................................24                     |
|      |                                                                                                                                                        | ..........................................................................30                                                                           |                                                                                                                                                        |
|      | 5.4.1 Validate in the P40 system ......................................................................................30                              | 5.4.1 Validate in the P40 system ......................................................................................30                              | 5.4.1 Validate in the P40 system ......................................................................................30                              |
|      | 5.4.2 Validate in the P08 system ......................................................................................33                              | 5.4.2 Validate in the P08 system ......................................................................................33                              | 5.4.2 Validate in the P08 system ......................................................................................33                              |
|      | Abbreviations/Acronyms ............................................................................................................35                  | Abbreviations/Acronyms ............................................................................................................35                  | Abbreviations/Acronyms ............................................................................................................35                  |
|    6 |                                                                                                                                                        |                                                                                                                                                        |                                                                                                                                                        |
|    8 | Version History ............................................................................................................................37         | Version History ............................................................................................................................37         | Version History ............................................................................................................................37         |

## 1. Overview

## 1.1 General Information

| Audience   | Global Process Users and Service Line Users   |
|------------|-----------------------------------------------|
| Frequency  | As and when required                          |

## 1.2 Related Internal Policies and Processes

| Upstream/Downstream processes   | Upstream : NA Downstream :   |
|---------------------------------|------------------------------|

## 1.3 Systems/Tools

## 1.3.1 Global Systems/Tools

| System/Tool   | System ID/Name   | Description           |
|---------------|------------------|-----------------------|
| Fiori         | P41              | Fiori Production      |
| MDG           | P45              | MDG Production        |
| SAP S/4 HANA  | P40              | S/4 HANA Production   |
| SAP ECC       | P08              | SAP Legacy Production |

## 1.3.2 Market-specific/Regional Systems/Tools

| System/Tool   | System ID   | Description   |
|---------------|-------------|---------------|
| NA            | NA          | NA            |

## 2. Executive Summary

## 2.1 Synopsis

The ABC Company has transactions with companies from all over the world. These transactions need to be tracked and the Country Code is a field used to identify transactions of ABC with an associate company from another country.

Any request to update a Country Code is raised in the Finance Request Form through Fiori. The request is initiated by the Requestor. The key field for the Country Code form is Title, as the Country Code itself cannot be a mandatory field at the Requestor level due to the business requirements.

The Requestor uses the search functionality to display all the Country Codes created within the Master Data Governance (MDG) framework to check if the Country Code (for which the request is raised) exists in the system. If the Country Code exists, the request to update the Country Code is created. However, if the Country Code does not exist, the Requestor then raises a request to create the Country Code. The ISO Country Code is the key field to be filled in the FRF as the Country Code itself cannot be a mandatory field at the Requestor level due to the business requirements. Once the Requestor enters the title, it cannot be changed.

When a Country Code needs to be updated, a request is created by the Requestor through the FRF in Fiori. The Requestor fills the FRF by answering a series of questions and submits the form to trigger the approval workflow.

The roles involved in updating a country code are:

- Requestor (Generic)
- Business Process Steward
- Business Process Leader (BPL)
- IT Configuration Team

The Business Process Steward receives the request through an e-mail notification in his/her inbox along with a hyperlink. He/she reviews the request and searches for the Country Code (for which the update request has been submitted) in Fiori.

If the queried Country Code is not found, the Business Process Steward adds relevant comments in the FRF and terminates the request by rejecting it. An e-mail notification along with a hyperlink is triggered to the Requestor to notify the action taken on the request.

However, if the queried Country Code is found, the Business Process Steward enriches the FRF and performs one of the following actions:

- Approve : The request is approved and routed to the Business Process Lead.
- Reject : The request is rejected and is automatically terminated. The Business Process Steward enters the appropriate comments citing the reason for rejection.
- Return : The request is sent back to the Requestor to gather additional information. The Business Process Steward adds his/her comments, seeking additional information that needs to be added to the change request.

This triggers an e-mail notification with a hyperlink to the Requestor, who then performs one of the following actions:

- Re-submit the request back to the Business Process Steward
- Withdraw the request

After the Business Process Steward approves the request, an e-mail notification is triggered to the Business Process Lead (BPL) that contains the hyperlink to access it. Based on his/her review, the BPL performs one of the following actions:

- Approve : The request is approved, triggering an e-mail notification to the Business Process Steward, Requestor, and IT Configuration Team to confirm that the request has been completed.
- Return : The request is sent back to the Requestor, seeking additional information in the change request.

If the change request is not approved, the BPL updates the Notes section, citing the missing requirements and clicks the Send for Revision button. An e-mail notification along with the hyperlink is triggered to the Requestor for review, who may then decide whether to resubmit or withdraw the request after reviewing the comments.

The Requestor reviews the request and validates if he/she wants to continue with the request. If no, the Requestor withdraws the request thus, ending/closing it. However, if the Requestor decides to continue with the request, he/she then enriches the request and resubmits it. This triggers an e-mail notification with the hyperlink of the action taken to the Business Process Lead.

Once the change request is approved by the BPL, the IT Configuration Team configures/updates the required Country Code in the S/4 HANA system by creating an incident through the Change Request Management (ChaRM) approval process in the Solution Manager. The configuration (Country Code update) that is done in the S/4 HANA system is transported to MDG using the SAP Landscape Transformation Replication Server (SLT). The IT Configuration Team performs the dual maintenance in the P08 system.

Note : The Country Code will be available for transaction after quarterly finance maintenance week (fourth week of every quarter on Thursday for quarter months, March, June, September, and December).

## 2.2 Objective

This process enables you to create and approve a Change Request to update a Country Code.

## 2.3 Process-specific Service Level Agreements (SLAs)

Note : Governance ppt link will be added here once it is received from the Business.

## 2.4 Risks and Controls

## 2.4.1 Global Risks and Controls

| Risk   | Control   |
|--------|-----------|

## 2.4.2 Market-Specific Risks and Controls

Risk

NA

## 2.5 Roles and Responsibilities

| Role                     | Responsibilities                                                                                                                                                                |
|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Requestor                | • Searches for the Country Code in Fiori • Populates the FRF in Fiori to Update Country Code                                                                                    |
| Business Process Steward | • Reviews the request • Enriches the Request • Rejects, returns or approves the request • Submits the request to the Business Process Lead                                      |
| Business Process Lead    | • Reviews the request received by from Business Process Steward • Validates and approves if the request is valid Return the request along with providing reasons for the return |

Control

NA

| IT Configuration Team   | • Updates the Country Code in S/4 HANA system. • Performs Dual Maintenance in P08   |
|-------------------------|-------------------------------------------------------------------------------------|

## 3. Inputs

| Input   | File Type and Location   | Frequency                   | Owner   | Purpose/Usage           |
|---------|--------------------------|-----------------------------|---------|-------------------------|
| Email   |                          | As per business requirement |         | Updating a Country Code |

## 4. Process Map

Given below is a high-level process map that describes this process:

![Image](outputs/pipeline_ocr_off/images/image_000000_3356dbd38aaf88a04ecd4d48ae0ebe5fc3d18d6fbba9047fbdb00b7fb17b998b.png)

*LLM image note:* Stub response for image_000000_3356dbd38aaf88a04ecd4d48ae0ebe5fc3d18d6fbba9047fbdb00b7fb17b998b.png. Replace describe_image_with_llm() with the OpenAI API call.


## 5. Process Description

## Disclaimer !

Please note that the screenshots used in this document are purely for illustration purposes. For example, the Change Request numbers between the screenshots of the 'email with the hyperlink' and other steps will not be aligned since the hyperlink feature is new and was not a part of the original release.

## 4.1 Submit the Request to Update a Country Code

The Requestor will perform the following actions to request Update the Country Code:

- 1.
- Log in to the P41 Fiori system using the Requestor ID and password. Note : To navigate directly to Fiori, click the following link:

https://t41ixa01.na.ko.com:4300/sap/bc/ui2/flp?sap-client=030&amp;sap-language=EN#Shell-

2. The default SAP Fiori home page is displayed. At the top-right side, click the drop-down arrow and select the FI: MD Finance Request Form list option.
3. From the FI: MD - Finance Request Forms tab, select the Manage Country Code tile.
4. The Search section: ISO Country Code page is displayed. In the ISO Country Code field, click the required Country Code.
5. Once the required Country Code is entered, click the Search button to search for the Country Code in Fiori.
6. The Results section displays the queried Country Code. If no Country Code is found, then the request is terminated, and the process for a new Country Code needs to be followed.
7. From the Result List section, click the queried Country Code hyperlink.
8. Country Code page is displayed. Click the Edit hyperlink to enrich the Finance Request Form.
9. Enrich the Finance Request Form by updating the Finance Data object fields.
10. Once the Change Request details are entered, click the Check hyperlink to detect any errors in the FRF.
11. If no errors are found, a notification appears on the bottom-left corner of the screen, indicating that there are no errors in the request.
12. Click the Submit button.
13. Notifications appear at the bottom-left corner of the screen, indicating that the Change Request has been submitted to the Business Process Steward.

![Image](outputs/pipeline_ocr_off/images/image_000001_21bb6ee60483d65527f36e1daaa4be05e363ceae5aa35476fa8709e2f7bfa998.png)

*LLM image note:* Stub response for image_000001_21bb6ee60483d65527f36e1daaa4be05e363ceae5aa35476fa8709e2f7bfa998.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000002_c2000aad9edf1bb0c74f520f5a9c0140a032125f39e0c95091ddca94977e5ff1.png)

*LLM image note:* Stub response for image_000002_c2000aad9edf1bb0c74f520f5a9c0140a032125f39e0c95091ddca94977e5ff1.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000003_1dacc82613881bc1523e2af685a52cdf32f2dbdecef651bae1fd76403abcc18a.png)

*LLM image note:* Stub response for image_000003_1dacc82613881bc1523e2af685a52cdf32f2dbdecef651bae1fd76403abcc18a.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000004_06ba38a1d2448e1b78ce643d900483b2b775a8264d314099cb77acb7bf3b33ab.png)

*LLM image note:* Stub response for image_000004_06ba38a1d2448e1b78ce643d900483b2b775a8264d314099cb77acb7bf3b33ab.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000005_f3c9ef99f8c7d54fa4c6d0e3bc2bdf0d3e173ff15b297b8f92b150b7ad254a9c.png)

*LLM image note:* Stub response for image_000005_f3c9ef99f8c7d54fa4c6d0e3bc2bdf0d3e173ff15b297b8f92b150b7ad254a9c.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000006_a427f20b1543740a62f71cf27c9defe6f8823b585301768fe9058a18ceb8b6d4.png)

*LLM image note:* Stub response for image_000006_a427f20b1543740a62f71cf27c9defe6f8823b585301768fe9058a18ceb8b6d4.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000007_6c7ac80e3d39eee5c61a88219b3436425c0832c658a063556b46617a072c52d9.png)

*LLM image note:* Stub response for image_000007_6c7ac80e3d39eee5c61a88219b3436425c0832c658a063556b46617a072c52d9.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000008_a9acb8a4f06a1c2c4a6c3bd65bc4cc729fc25f2dc9a5a6ffc68d3741a478c083.png)

*LLM image note:* Stub response for image_000008_a9acb8a4f06a1c2c4a6c3bd65bc4cc729fc25f2dc9a5a6ffc68d3741a478c083.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000009_f7ebdf0e73d70a48aed84c6f5163c581a0f2b52ad4da967f5c5dc509a250e78b.png)

*LLM image note:* Stub response for image_000009_f7ebdf0e73d70a48aed84c6f5163c581a0f2b52ad4da967f5c5dc509a250e78b.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000010_a9e7619556945d8cf97c7ab434796a503738ccb47d171fdb1a85c082391b372b.png)

*LLM image note:* Stub response for image_000010_a9e7619556945d8cf97c7ab434796a503738ccb47d171fdb1a85c082391b372b.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000011_0d27b46119b5e463532b67975faadd44fb1a31c2dde1a42da6f8dafd7d7d26b1.png)

*LLM image note:* Stub response for image_000011_0d27b46119b5e463532b67975faadd44fb1a31c2dde1a42da6f8dafd7d7d26b1.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000012_09aa3ff3142aa71124a6b5a4025c64998a8f9cbd838acd2d0f1e73881d1f21ea.png)

*LLM image note:* Stub response for image_000012_09aa3ff3142aa71124a6b5a4025c64998a8f9cbd838acd2d0f1e73881d1f21ea.png. Replace describe_image_with_llm() with the OpenAI API call.


## 4.2 Review the Submitted Change Request

Once the request to update Country Code is submitted by a Requestor, a system triggered e-mail notification with a hyperlink to access the change request is sent to the Business Process Steward. The email notification will also contain any notes added in the Finance Request Form while submitting the request by requestor. Business Process Steward needs to check the notes to go through the relevant information.

A sample of the e-mail notification is displayed below:

![Image](outputs/pipeline_ocr_off/images/image_000013_e7f72758dee235ff05081f453d10f79d2045cb9cf8e0734b6c2b595267b6761e.png)

*LLM image note:* Stub response for image_000013_e7f72758dee235ff05081f453d10f79d2045cb9cf8e0734b6c2b595267b6761e.png. Replace describe_image_with_llm() with the OpenAI API call.


User can access the change request either through the hyperlink from the email notification or going through the Fiori Launch Pad. Enable Now SOP will contain both the process to access the Change Request, for User Training.

The subsequent steps are shown with Fiori steps, however to proceed to the next step using the hyperlink from the email, go to section 4.2.4.

To review the submitted request, as a Business Process Steward, perform the following steps:

- Log in to the P41 Fiori system using your Business Process Steward ID and password. Note : To navigate directly to Fiori, click the following link:
- 1.

https://t41ixa01.na.ko.com:4300/sap/bc/ui2/flp?sap-client=030&amp;sap-language=EN#Shell-

2. From the Finance Request Form tab, select the Change Requests tile.
3. The MDG: Change Requests page is displayed and shows all the Change Request items, including the request to update the Country Code. In the Subject column, click the Process Change Request number hyperlink.
4. The Country Code page is displayed and shows the default General tab. Review the request in the General , Notes , and the Attachments tab.

![Image](outputs/pipeline_ocr_off/images/image_000014_9e3c7420f7c678c250932020a082ebca4df81c19a2bd5bc84e8b55bc0829cafd.png)

*LLM image note:* Stub response for image_000014_9e3c7420f7c678c250932020a082ebca4df81c19a2bd5bc84e8b55bc0829cafd.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000015_926866f31a54af94d7fe996c77a6cf04bcf01226c47989744c1e384e7745f700.png)

*LLM image note:* Stub response for image_000015_926866f31a54af94d7fe996c77a6cf04bcf01226c47989744c1e384e7745f700.png. Replace describe_image_with_llm() with the OpenAI API call.


Note : While reviewing the submitted request, the Business Process Steward ensures that the change request is a valid request. The Business Process Steward reviews that the Country Code updated details mentioned in the General Data , Notes , and Attachments are correct. If any of the required parameters are missing or are wrong, the request is terminated or returned along with comments supporting the rejection/return. If the request is valid, the request is submitted for further processing.

![Image](outputs/pipeline_ocr_off/images/image_000016_4b4a0dca0a56b2b0c877b5d4aa40943c7f7717d9ba5198cb850563b72dfcac1f.png)

*LLM image note:* Stub response for image_000016_4b4a0dca0a56b2b0c877b5d4aa40943c7f7717d9ba5198cb850563b72dfcac1f.png. Replace describe_image_with_llm() with the OpenAI API call.


5. If the request submitted by the Requestor is not valid, click the Reject button.
6. A New Note pop-up is displayed. It is mandatory to provide supporting comments for the rejection. Add supporting comments for the rejection in the New Note box and click the OK button.
7. Notifications appear at the bottom-left corner of the screen, indicating that the request has been rejected. This request is terminated, and the Requestor must create a new request.

![Image](outputs/pipeline_ocr_off/images/image_000017_37ec3ddb5709326318dfb53ccc0875e966bf4645f057f69f840bada03039ef0f.png)

*LLM image note:* Stub response for image_000017_37ec3ddb5709326318dfb53ccc0875e966bf4645f057f69f840bada03039ef0f.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000018_46a15c63e965c4e07febb0dff304b2c91e958bd8239ed1e4406b1ab30908f9f9.png)

*LLM image note:* Stub response for image_000018_46a15c63e965c4e07febb0dff304b2c91e958bd8239ed1e4406b1ab30908f9f9.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000019_be94035405e20a8c6a1e6c49715b31f2f891be8ba7735b30076e6e24a71070e8.png)

*LLM image note:* Stub response for image_000019_be94035405e20a8c6a1e6c49715b31f2f891be8ba7735b30076e6e24a71070e8.png. Replace describe_image_with_llm() with the OpenAI API call.


This triggers an automatic e-mail notification to the Requestor informing them about the status of the change request. The e-mail contains the hyperlink to access the change request. A sample of the e-mail notification is displayed below:

![Image](outputs/pipeline_ocr_off/images/image_000020_55200e652b09dfda1c55ef0b08cbf5b9345dcb275bacac0fbea64a10deec4f69.png)

*LLM image note:* Stub response for image_000020_55200e652b09dfda1c55ef0b08cbf5b9345dcb275bacac0fbea64a10deec4f69.png. Replace describe_image_with_llm() with the OpenAI API call.


If the request is a valid request, the Business Process Steward proceeds to enrich the request to update the Country Code that already exists in the MDG system.

8. The Business Process Steward enriches the request by adding additional information in the Change Request fields.
9. If the Change Request still lacks some information that needs to be added, the Business Process Steward clicks the Send for Revision button.
10. A New Note pop-up is displayed. It is mandatory to provide supporting comments for the return. Add supporting comments for the return of the request in the New Note box and click the OK button.
11. Notifications appear at the bottom-left corner of the screen, indicating that the Change Request has been sent back to the Requestor for revision.

![Image](outputs/pipeline_ocr_off/images/image_000021_c10c7507976bea2976d2506a43d6c2dff712abed9d799ad31a7d2156fa62a0cf.png)

*LLM image note:* Stub response for image_000021_c10c7507976bea2976d2506a43d6c2dff712abed9d799ad31a7d2156fa62a0cf.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000022_309aa7fedd1daebaa5915ceaa2a92aa6aa210400b251771dbfb5a7ec5871854b.png)

*LLM image note:* Stub response for image_000022_309aa7fedd1daebaa5915ceaa2a92aa6aa210400b251771dbfb5a7ec5871854b.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000023_699c4920721057a3262ec5d6596a340a1e960c4bd2258637d65c030e775f29d8.png)

*LLM image note:* Stub response for image_000023_699c4920721057a3262ec5d6596a340a1e960c4bd2258637d65c030e775f29d8.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000024_04c8029d2eeabbd3526655fe15d5214cd6a817aa2a1c15354a062084548a7a6a.png)

*LLM image note:* Stub response for image_000024_04c8029d2eeabbd3526655fe15d5214cd6a817aa2a1c15354a062084548a7a6a.png. Replace describe_image_with_llm() with the OpenAI API call.


After the Business Process Steward sends the request back, the change request is returned to the Requestor. This triggers an automatic e-mail notification containing the hyperlink to access the change request to the Requestor informing him/her about the status of the change request. The Requestor then decides upon withdrawal or resubmitting it for approval.

A sample of the e-mail notification is displayed below:

![Image](outputs/pipeline_ocr_off/images/image_000025_f75e0f213e59a701b107ba31b440fbcb6b6f21c17edbbb496bfcf53eea37ef0c.png)

*LLM image note:* Stub response for image_000025_f75e0f213e59a701b107ba31b440fbcb6b6f21c17edbbb496bfcf53eea37ef0c.png. Replace describe_image_with_llm() with the OpenAI API call.


Once the request is sent back to the Requestor, the Requestor will decide whether to resubmit the request or not.

12. Requestor can re-submit the request or withdraw the request upon receiving the request sent back to him for revision from BPS.

User can access the change request either through the hyperlink from the email notification or going through the Fiori Launch Pad. Enable Now SOP will contain both the process to access the Change Request, for User Training.

The subsequent steps are shown with Fiori steps, however to proceed to the next step using the hyperlink, go to section 4.2.12.3 below.

1. To re-submit the request, he/she performs the following steps:
2. From the MDG: Change Requests page, click the appropriate Process Change Request hyperlink.
3. Click the Resubmit button after making the necessary revisions to the change request.
13. If the request is valid and has no errors, the Business Process Steward approves the request by clicking the Approve button.
14. Notifications appear at the bottom-left corner of the screen, indicating that the Change Request has been approved.

![Image](outputs/pipeline_ocr_off/images/image_000026_a150d2d2504de05bef58d9875a1ec17192ab97cf432f0475ced85a0dde5d23f9.png)

*LLM image note:* Stub response for image_000026_a150d2d2504de05bef58d9875a1ec17192ab97cf432f0475ced85a0dde5d23f9.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000027_5154317b7ae8d3eaa9e7e736a4aef0a1a298eb7f6b1630f1c19e86faf3cd0f31.png)

*LLM image note:* Stub response for image_000027_5154317b7ae8d3eaa9e7e736a4aef0a1a298eb7f6b1630f1c19e86faf3cd0f31.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000028_2ec598d1d84f7f916e80155bf486918ac717debe5cef71c533f724ae12282a0d.png)

*LLM image note:* Stub response for image_000028_2ec598d1d84f7f916e80155bf486918ac717debe5cef71c533f724ae12282a0d.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000029_e57f608e839927a9672dd0f2bb5383cbbc2cc2780c516edc4723c297efa779e4.png)

*LLM image note:* Stub response for image_000029_e57f608e839927a9672dd0f2bb5383cbbc2cc2780c516edc4723c297efa779e4.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000030_63d759e9b0365a5fac4318e57a882f8a4c79a95d1193ac1e878ea21f553c4e24.png)

*LLM image note:* Stub response for image_000030_63d759e9b0365a5fac4318e57a882f8a4c79a95d1193ac1e878ea21f553c4e24.png. Replace describe_image_with_llm() with the OpenAI API call.


The Change Request is then forwarded to the Business Process Lead for further review.

## 4.3 Obtain Requisite Approval

After the Business Process Steward approves the change request, an e-mail notification with a hyperlink to access the change request is triggered to the BPL. The email notification will also contain any notes added in the Finance Request Form while submitting the request by requestor.

A sample of the e-mail notification is displayed below:

User can access the change request either through the hyperlink from the email notification or going through the Fiori Launch Pad. Enable Now SOP will contain both the process to access the Change Request for User Training.

The subsequent steps are shown with Fiori steps, however to proceed to the next step using the hyperlink, go to section 4.3.5.

He/she reviews the request and decides upon approving or sending the same for revision.

To review the submitted request, as a BPL, perform the following steps:

To review and approve the request to update the Country Code, the Business Process Lead needs to perform the following steps:

1. Log in to the P41 Fiori system with the Business Process Lead ID and password.
2. The default SAP Fiori Home page is displayed. At the top-right side, click the drop-down arrow and select the FI: MD Finance Request Form list option.
3. From the FI: MD - Finance Request Form tab, select the Change Request tile.
4. The MDG: Change Requests page is displayed and shows all the Change Request items, including the request to update the Country Code. In the Subject column, click the Process Change Request number hyperlink.
5. The Country Code page is displayed and shows the default General tab. Review the request in the General , Notes , and the Attachments tab.
6. If the Change Request lacks some information that needs to be added, the Business Process Lead clicks the Send for Revision button.
7. A New Note pop-up is displayed. It is mandatory to provide supporting comments for the return. Add supporting comments for the return of the request in the New Note box and click the OK button.
8. Notifications appear at the bottom-left corner of the screen, indicating that the request has been sent back to the Requestor for revision.

Note : To navigate directly to Fiori, click the following link:

https://t41ixa01.na.ko.com:4300/sap/bc/ui2/flp?sap-client=030&amp;sap-language=EN#Shell-

![Image](outputs/pipeline_ocr_off/images/image_000031_726fe59722ee0e916e85ba83864e78a252c9494babae224649a462661159d364.png)

*LLM image note:* Stub response for image_000031_726fe59722ee0e916e85ba83864e78a252c9494babae224649a462661159d364.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000032_98a64358e034d17bca9e55345c4de24f5e61e1afdf68cfdf4598c274e3e479a7.png)

*LLM image note:* Stub response for image_000032_98a64358e034d17bca9e55345c4de24f5e61e1afdf68cfdf4598c274e3e479a7.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000033_10efd8aa78768665de5a812765c44b5561fcedf63698c48a4cebad047fc4e2a4.png)

*LLM image note:* Stub response for image_000033_10efd8aa78768665de5a812765c44b5561fcedf63698c48a4cebad047fc4e2a4.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000034_5a84706f3f89a23567e2153d8eaac2304de1d0dbfe2dfac3c4a98443f659b855.png)

*LLM image note:* Stub response for image_000034_5a84706f3f89a23567e2153d8eaac2304de1d0dbfe2dfac3c4a98443f659b855.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000035_91bfb6d7da712d071dc5c45cdea3d44262e1d035d711e2144357aa81056c2b8d.png)

*LLM image note:* Stub response for image_000035_91bfb6d7da712d071dc5c45cdea3d44262e1d035d711e2144357aa81056c2b8d.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000036_8aeed8a2752e0a9e33bc114262261e7ff5c1774c817d5a0a341e9356538add5f.png)

*LLM image note:* Stub response for image_000036_8aeed8a2752e0a9e33bc114262261e7ff5c1774c817d5a0a341e9356538add5f.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000037_4f9b81a436c574e4f7a80596e82d0b259db69c4fba5fa9606805c867af8c195e.png)

*LLM image note:* Stub response for image_000037_4f9b81a436c574e4f7a80596e82d0b259db69c4fba5fa9606805c867af8c195e.png. Replace describe_image_with_llm() with the OpenAI API call.


The change request is returned to the Requestor. This triggers an automatic e-mail notification containing the hyperlink to access the change request to the Requestor informing him/her about its status.The Requestor then decides upon withdrawal or resubmitting it for approval.

A sample of the e-mail notification is displayed below:

![Image](outputs/pipeline_ocr_off/images/image_000038_f6ae5baec2116022c007d9f790316b342599478f1f425c0e14d5df4cf0813340.png)

*LLM image note:* Stub response for image_000038_f6ae5baec2116022c007d9f790316b342599478f1f425c0e14d5df4cf0813340.png. Replace describe_image_with_llm() with the OpenAI API call.


Requestor can resubmit the request or withdraw the request upon receiving the request sent back to him for revision from BPL. Please follow the steps for submitting/withdrawing the request as from section 4.2.12.

9. If the request is valid and has no errors, the Business Process Steward approves the request by clicking the Approve button.
10. Notifications appear at the bottom-left corner of the screen, indicating that the request has been approved.

![Image](outputs/pipeline_ocr_off/images/image_000039_db970e70d41850b7e13745a122174640a5381e3b47b4a72af7e0994c7f9e2a1e.png)

*LLM image note:* Stub response for image_000039_db970e70d41850b7e13745a122174640a5381e3b47b4a72af7e0994c7f9e2a1e.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000040_fee09b56bca40a2683060a79f96880d27dff646eb1f52ad053e70b5d06bc85f1.png)

*LLM image note:* Stub response for image_000040_fee09b56bca40a2683060a79f96880d27dff646eb1f52ad053e70b5d06bc85f1.png. Replace describe_image_with_llm() with the OpenAI API call.


Once the request is approved. An automatic email notification is triggered to the Business Process Steward and Requestor to confirm that the request has been approved.

![Image](outputs/pipeline_ocr_off/images/image_000041_b8f4a6a19ceb71deb87377bb39d6858c6bb0a9ddff11b05b5857b2b72ae81339.png)

*LLM image note:* Stub response for image_000041_b8f4a6a19ceb71deb87377bb39d6858c6bb0a9ddff11b05b5857b2b72ae81339.png. Replace describe_image_with_llm() with the OpenAI API call.


## 4.4 Replicate in S/4 HANA and P08 Systems

After the BPL provides the approval, the IT Configuration Team will update the required Country Code in the S/4 HANA (P40) and P08 systems by creating an incident through the ChaRM approval process in the Solution Manager. The configuration (update Country Code) will be transported to the MDG using the SAP Landscape Transformation Replication Server (SLT). The IT Configuration Team will perform the Dual maintenance in the P08 system. The new Country Code field will be available in the system for transaction after the quarterly maintenance Finance week i.e. the 4 th  Week of every quarter on a Thursday for the quarter months March, June, Sep and Dec.

## 4.4.1 Validate in the P40 system

To validate the replication of the update of the Country Code in the SAP S/4 HANA or P40 system, the Global IT Configuration Team or Requestor performs the following steps.

1. The SAP Easy Access screen is displayed. In the Command Box , enter the Transaction code and press the Enter key.
2. The General Table Display screen is displayed. In the Table field, enter the updated Country Code recorded in P40 system.
3. Once the Country Code is entered, click the Execute button shown as an icon in the top-left corner of the screen.
4. The updated Country Code is replicated in SAP S/4 HANA (P40) system.

![Image](outputs/pipeline_ocr_off/images/image_000042_eb92dd51572b677bc3c834bbfddfea3240427c5993b678f37185e4311fd1b483.png)

*LLM image note:* Stub response for image_000042_eb92dd51572b677bc3c834bbfddfea3240427c5993b678f37185e4311fd1b483.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000043_52066daf4d39e624d917dbfbcba612d62208f2ec41f7ba9a402ddf9bc0b795c6.png)

*LLM image note:* Stub response for image_000043_52066daf4d39e624d917dbfbcba612d62208f2ec41f7ba9a402ddf9bc0b795c6.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000044_8ef369e0b6ff57f350be58cfdd6b09e796ebb2022ba7c026cb9c46a3220d9cba.png)

*LLM image note:* Stub response for image_000044_8ef369e0b6ff57f350be58cfdd6b09e796ebb2022ba7c026cb9c46a3220d9cba.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000045_f57736960f6cdb27f7b6ed1d96bb06c2d7f654e0f57f86ad9093ae67106e4136.png)

*LLM image note:* Stub response for image_000045_f57736960f6cdb27f7b6ed1d96bb06c2d7f654e0f57f86ad9093ae67106e4136.png. Replace describe_image_with_llm() with the OpenAI API call.


The updated Country Code will be available in the system for transaction after the quarterly maintenance Finance week i.e. the 4th Week of every quarter on a Thursday for the quarter months March, June, September and December.

## 4.4.2 Validate in the P08 system

To validate the replication of the update of the Country Code in the P08 system, the Global IT Configuration Team performs the following steps.

1. The SAP Easy Access screen is displayed. In the Command Box , enter the Transaction code and press the Enter key.
2. The General Table Display screen is displayed. In the Table field, enter the updated Country Code recorded in P08 system.
3. Once the Country Code is entered, click the Execute button shown as an icon in the top-left corner of the screen.
4. The updated Country Code is replicated in the P08 system.

![Image](outputs/pipeline_ocr_off/images/image_000046_a29f2004ffc7c6b202bf8b4c9e2c8fb7e2eec26d85c6b935a5435f149d905d6d.png)

*LLM image note:* Stub response for image_000046_a29f2004ffc7c6b202bf8b4c9e2c8fb7e2eec26d85c6b935a5435f149d905d6d.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000047_93ec1298a8c254d4750ec2e15e263fbb272264ebd09b8439bad097b60d129f3e.png)

*LLM image note:* Stub response for image_000047_93ec1298a8c254d4750ec2e15e263fbb272264ebd09b8439bad097b60d129f3e.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000048_50301af3d13e003928e55535a3a3dfa35e6cbc7b74851e0716aff20f5661dfbb.png)

*LLM image note:* Stub response for image_000048_50301af3d13e003928e55535a3a3dfa35e6cbc7b74851e0716aff20f5661dfbb.png. Replace describe_image_with_llm() with the OpenAI API call.


![Image](outputs/pipeline_ocr_off/images/image_000049_28ed53ec4779858d2ec432c4ede83a4277625f6af02c32aff8620ace5e3f8369.png)

*LLM image note:* Stub response for image_000049_28ed53ec4779858d2ec432c4ede83a4277625f6af02c32aff8620ace5e3f8369.png. Replace describe_image_with_llm() with the OpenAI API call.


## 6. Abbreviations/Acronyms

| Short Form   | Full Form                                       |
|--------------|-------------------------------------------------|
| BPL          | Business Process Lead                           |
| FRF          | Finance Request Form                            |
| SLT          | SAP Landscape Transformation Replication Server |

## 7. Outputs

| Output Name   | Output Type   | Output Location   |
|---------------|---------------|-------------------|
|               |               | SAP S/4 HANA      |
|               |               | SAP P08           |

## Version History

|   Version | Date                     | Change Owner             | Change Request No.   | Change Details     |
|-----------|--------------------------|--------------------------|----------------------|--------------------|
|         1 | Month in words/Date/Year | Name of the change owner | Change request ID    | Change description |
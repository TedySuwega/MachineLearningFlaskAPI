import urllib3, requests, json

# NOTE: generate iam_token and retrieve ml_instance_id based on provided documentation
header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + iam_token, 'ML-Instance-ID': ml_instance_id}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"fields":
                       ["bpd_id",
                        "bldf_grading_sales_to_payor",
                        "bld_loan_tenor",
                        "bpd_website_url_flag",
                        "bld_bpd_id",
                        "early_loan_total",
                        "bld_invoice_amount_Mean",
                        "bld_invoice_amount_Min",
                        "bld_invoice_amount_Max",
                        "bid_invoice_tenor_mean",
                        "bid_invoice_tenor_min",
                        "bid_invoice_tenor_max",
                        "bld_loan_disbursement_amount_sum",
                        "bld_loan_disbursement_amount_mean",
                        "bld_loan_disbursement_amount_min",
                        "bld_loan_disbursement_amount_max",
                        "bld_loan_tenor_mean",
                        "bld_loan_tenor_min",
                        "bld_loan_tenor_max",
                        "marketplace_fee_sum",
                        "marketplace_fee_max",
                        "bcd_doc_uploaded_Mean",
                        "bcd_doc_uploaded_Max",
                        "mob",
                        "bmbl_age_mean",
                        "bmbl_age_min",
                        "bmbl_age_max",
                        "good_loan_proportion",
                        "loan_active",
                        "loan_inactive",
                        "loan_count",
                        "dpd_min",
                        "dpd_max",
                        "dpd_total",
                        "dpd_average"],
                   "values": [array_of_values_to_be_scored, another_array_of_values_to_be_scored]}

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/v3/wml_instances/39ba2543-9dea-45ce-bb14-72d5a7ecb417/deployments/6e3ccf9b-1f3f-4c4b-b3ea-dbb9b58f7311/online', json=payload_scoring, headers=header)
print("Scoring response")
print(json.loads(response_scoring.text))
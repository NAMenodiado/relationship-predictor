import pandas as pd

def manual_one_hot_encode(data):
    # Initializing the DataFrame
    final_data = pd.DataFrame()

    # Putting in the non-categorical columns.
    final_data['openness'] = pd.to_numeric(data['How open are you to trying new things? '], errors='coerce')
    final_data['partner_openness'] = pd.to_numeric(data['[PARTNER] How open is he/she/they to trying new things? '], errors='coerce')

    # Manual onehot encoding that I already prepared. 
    final_data['in_out_tag_Outdoors'] = data.apply(
        lambda x: 1 if x['Do you enjoy the outdoors more or indoors?'] == 'Outdoors' else 0,
        axis=1
    )
    final_data['art_sport_tag_Sporty'] = data.apply(
        lambda x: 1 if x['Would you say that you are more the "artistic" type or the "sporty" type?'] == 'Sporty' else 0,
        axis=1
    )
    final_data['introversion_ME Time'] = data.apply(
        lambda x: 1 if x['Do you enjoy going out more or having more "me" or "alone" time?'] == 'ME Time' else 0,
        axis=1
    )
    final_data['cooking_Yes'] = data.apply(
        lambda x: 1 if x['Do you enjoy cooking? (For yourself or even for others?)'] == 'Yes' else 0,
        axis=1
    )
    final_data['pref_rel_len_Short Term'] = data.apply(
        lambda x: 1 if x['Are you someone who currently wants to have a long term relationship or nah? '] == 'Short Term' else 0,
        axis=1
    )
    final_data['children_Yes'] = data.apply(
        lambda x: 1 if x['Do you want to have children in the future? '] == 'Yes' else 0,
        axis=1
    )
    final_data['value_Family'] = data.apply(
        lambda x: 1 if x['Do you value career more or family?'] == 'Family' else 0,
        axis=1
    )
    final_data['smoke_Yes'] = data.apply(
        lambda x: 1 if x['Do you smoke?'] == 'Yes' else 0,
        axis=1
    )
    final_data['drink_Yes'] = data.apply(
        lambda x: 1 if x['Do you drink? (Like really enjoy it)'] == 'Yes' else 0,
        axis=1
    )
    final_data['sleeping_Late at night'] = data.apply(
        lambda x: 1 if x['Do you prefer staying up late at night? Or do you prefer waking up early in the morning?'] == 'Late at night' else 0,
        axis=1
    )
    final_data['pets_Yes'] = data.apply(
        lambda x: 1 if x['Do you like pets?'] == 'Yes' else 0,
        axis=1
    )
    final_data['conflict_Confront'] = data.apply(
        lambda x: 1 if x['Do you avoid conflict or confronts issues?'] == 'Confront' else 0,
        axis=1
    )
    final_data['expression_Private'] = data.apply(
        lambda x: 1 if x['Do you express your emotions openly or in private?'] == 'Private' else 0,
        axis=1
    )
    final_data['partner_in_out_Outdoors'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they enjoy the outdoors more or indoors?'] == 'Outdoors' else 0,
        axis=1
    )
    final_data['partner_introversion_ME Time'] = data.apply(
        lambda x: 1 if x['[PARTNER]  Does he/she/they enjoy going out more or having more "me" or "alone" time?'] == 'ME Time' else 0,
        axis=1
    )
    final_data['partner_cooking_Yes'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they enjoy cooking?'] == 'Yes' else 0,
        axis=1
    )
    final_data['partner_pref_rel_len_Short Term'] = data.apply(
        lambda x: 1 if x['[PARTNER]  Is he/she/they someone who currently wants to have a long term relationship or nah? '] == 'Short Term' else 0,
        axis=1
    )
    final_data['partner_children_Yes'] = data.apply(
        lambda x: 1 if x['[PARTNER]  Does he/she/they want to have children in the future? '] == 'Yes' else 0,
        axis=1
    )
    final_data['partner_value_Family'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they value career more or family?'] == 'Family' else 0,
        axis=1
    )
    final_data['partner_smoke_Yes'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they smoke?'] == 'Yes' else 0,
        axis=1
    )
    final_data['partner_drink_Yes'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they drink?  (Like really enjoy it)'] == 'Yes' else 0,
        axis=1
    )
    final_data['partner_sleeping_Late at night'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they prefer staying up late at night? Or do you prefer waking up early in the morning?'] == 'Late at night' else 0,
        axis=1
    )
    final_data['partner_pet_Yes'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they like pets?'] == 'Yes' else 0,
        axis=1
    )
    final_data['partner_art_sport_tag_Sporty'] = data.apply(
        lambda x: 1 if x['[PARTNER] Would you say that he/she/they is more the "artistic" type or the "sporty" type?'] == 'Sporty' else 0,
        axis=1
    )
    final_data['partner_conflict_Confront'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they avoid conflict or confronts issues?'] == 'Confront' else 0,
        axis=1
    )
    final_data['partner_expression_Private'] = data.apply(
        lambda x: 1 if x['[PARTNER] Does he/she/they express his/her/their emotions openly or in private?'] == 'Private' else 0,
        axis=1
    )
    final_data['partner_status_Ex'] = data.apply(
        lambda x: 1 if x['Is this someone you are currently with or not yet?'] == 'Not Yet' else 0,
        axis=1
    )

    return final_data
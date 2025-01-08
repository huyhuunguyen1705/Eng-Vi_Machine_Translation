import pyarrow.parquet as pq
import pyarrow as pa

def filter_sentences(input_file, output_file, max_length=300):
    # Read the Parquet file
    table = pq.read_table(input_file)
    data = table.to_pydict()
    
    # Filter items
    filtered_data = {
        'translation': []
    }
    filtered_count = 0  # Counter for filtered items

    for item in data['translation']:
        en_sentence = item['en']
        vi_sentence = item['vi']
        if len(en_sentence) + len(vi_sentence) <= max_length:
            filtered_data['translation'].append(item)
            filtered_count += 1  # Increment the counter

    # Create a new Arrow Table with filtered data
    new_table = pa.table(filtered_data)
    
    # Write the new table to a Parquet file
    pq.write_table(new_table, output_file)

    # Print the number of filtered items
    print(f"Number of filtered items: {filtered_count}")

# Example usage
input_parquet = 'mt_en_vi.parquet'
output_parquet = 'filtered_mt_en_vi.parquet'
filter_sentences(input_parquet, output_parquet)

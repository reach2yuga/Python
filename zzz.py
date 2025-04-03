from fpdf import FPDF

# Create a PDF document
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# Set title
pdf.set_font('Arial', 'B', 16)
pdf.cell(200, 10, txt="Snowflake Data Engineer Exam Questions", ln=True, align='C')

# Add questions and options
pdf.ln(10)
pdf.set_font('Arial', '', 12)

questions = [
    {
        "q": "Question 1: To view/monitor the clustering metadata for a table, Snowflake provides which of the following system functions?",
        "options": [
            "A) SYSTEM$CLUSTERING_DEPTH_KEY",
            "B) SYSTEM$CLUSTERING_KEY_INFORMATION (including clustering depth)",
            "C) SYSTEM$CLUSTERING_DEPTH",
            "D) SYSTEM$CLUSTERING_INFORMATION (including clustering depth)"
        ],
        "answer": "Answer: C, D",
        "explanation": "SYSTEM$CLUSTERING_DEPTH: Computes the average depth of the table according to the specified columns..."
    },
    {
        "q": "Question 2: Select the incorrect statements regarding Clustering depth?",
        "options": [
            "A) The clustering depth for a populated table measures the average depth (1 or greater) of the overlapping micro-partitions...",
            "B) It helps Monitoring the clustering 'health' of a large table, particularly over time as DML is performed on the table.",
            "C) Clustering depth can be used for determining whether a large table would benefit from explicitly defining a clustering key.",
            "D) A table with no micro-partitions (i.e. an unpopulated/empty table) has a clustering depth of 1."
        ],
        "answer": "Answer: D",
        "explanation": "A table with no micro-partitions (i.e. an unpopulated/empty table) has a clustering depth of 0."
    },
    {
        "q": "Question 3: While creating even Secure UDF, Snowflake recommends using randomized identifiers instead of sequence-generated values?",
        "options": [
            "A) TRUE",
            "B) FALSE"
        ],
        "answer": "Answer: A",
        "explanation": "Snowflake recommends using randomized identifiers for better security."
    },
    {
        "q": "Question 4: Which UDF programming language is not supported with Snowflake Secure Data Sharing feature?",
        "options": [
            "A) SQL",
            "B) JAVA",
            "C) JAVASCRIPT",
            "D) PYTHON"
        ],
        "answer": "Answer: C",
        "explanation": "JAVASCRIPT is not supported for Snowflake Secure Data Sharing."
    },
    {
        "q": "Question 5: Which are supported Programming Languages for Creating UDTFs?",
        "options": [
            "A) Python",
            "B) Node.javascript",
            "C) Javascript",
            "D) Java",
            "E) Perl"
        ],
        "answer": "Answer: A, C, D",
        "explanation": "Python, Javascript, and Java are supported for creating UDTFs."
    },
    {
        "q": "Question 6: Tasks may optionally use table streams to provide a convenient way to continuously process new or changed data. Which System Function can be used by Data Engineer to verify whether a stream contains changed data for a table?",
        "options": [
            "A) SYSTEM$STREAM_HAS_CHANGE_DATA",
            "B) SYSTEM$STREAM_CDC_DATA",
            "C) SYSTEM$STREAM_HAS_DATA",
            "D) SYSTEM$STREAM_DELTA_DATA"
        ],
        "answer": "Answer: C",
        "explanation": "SYSTEM$STREAM_HAS_DATA indicates whether a specified stream contains change data capture records."
    },
    {
        "q": "Question 7: Streams cannot be created to query change data on which of the following objects? [Select All that Apply]",
        "options": [
            "A) Standard tables, including shared tables.",
            "B) Views, including secure views",
            "C) Directory tables",
            "D) Query Log Tables",
            "E) External tables"
        ],
        "answer": "Answer: D",
        "explanation": "Streams do not support Query Log tables."
    },
    {
        "q": "Question 8: To advance the offset of a stream to the current table version without consuming the change data in a DML operation, which of the following operations can be done by Data Engineer?",
        "options": [
            "A) Using the CREATE OR REPLACE STREAM syntax, recreate the STREAM",
            "B) Insert the current change data into a temporary table...",
            "C) A stream advances the offset only when it is used in a DML transaction...",
            "D) Delete the offset using STREAM properties SYSTEM$RESET_OFFSET(<stream_id>)"
        ],
        "answer": "Answer: A, B",
        "explanation": "Recreating the stream or inserting the current change data into a temporary table will advance the offset."
    }
]

# Add each question and its options, answers, and explanations
for question in questions:
    pdf.multi_cell(0, 10, question["q"])
    for option in question["options"]:
        pdf.multi_cell(0, 10, option)
    pdf.multi_cell(0, 10, question["answer"])
    pdf.multi_cell(0, 10, "Explanation: " + question["explanation"])
    pdf.ln(10)

# Output the PDF
pdf_output = "/workspaces/Python/Infosys interview que/Snowflake_Exam_Questions.pdf"
pdf.output(pdf_output)

pdf_output

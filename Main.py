import streamlit as st
import llm  # Make sure this module is correctly set up and accessible

# Define the function that uses the LLM
def generate_analysis(specific_offering):
    prompt = f'''
    You are an advanced AI assistant to help an innovator with preliminary market analysis for {specific_offering}, following this structure:

    # Executive Summary
    # Market Analysis
    # Competition Analysis
    # Company Perspective
    # Technology Perspective (if applicable)
    # Financial Projections
    # Risk Assessment
    # Summary and Recommendations

    Guidelines:
    1. For each section, provide detailed insights and data-driven analysis specific to [specific offering]. 
    2. Use credible sources such as market research reports, industry publications, company financial statements, and expert opinions to support your analysis. 
    3. Include market size estimates, growth rates, competitor information, technological aspects, financial projections, and risk assessments relevant to {specific_offering}.

    Instructions:
    1. Identify the product, service, or technology you want to analyze and improve.

    2. Identify 4-5 key categories that encompass essential aspects of the chosen product, service, or technology. These categories should cover areas such as functionality, user experience, performance, design, or any other relevant aspects.

    3. For each category, identify 3-4 relevant attributes that significantly impact the product, service, or technology. These attributes should be specific and measurable aspects that contribute to the overall effectiveness and user satisfaction.

    4. For each attribute, provide a diverse range of 4-5 values that cover various aspects and possibilities. Ensure that the values are distinct and offer different perspectives on the attribute.

    5. Present the categories, attributes, and their values in a clear and organized tabular format, making it easy to understand and analyze the information.

    6. Create 5-6 unique combinations of attribute values from different categories to generate innovative ideas for the product, service, or technology. Start with realistic combinations that are more common in the current market landscape and gradually progress towards more innovative and futuristic combinations.

    7. For each combination, provide a brief but informative analysis of its usefulness and potential applications. Highlight the specific benefits, target audience, or situations where the combination would be most effective.

    8. When creating combinations, ensure that they are diverse and cover a wide range of attributes from different categories. Each combination should demonstrate creative thinking and cater to various user needs and scenarios.

    9. As you progress towards more innovative combinations, consider incorporating advanced technologies, emerging trends, or unconventional approaches. This showcases an understanding of the evolving market landscape and a forward-thinking mindset.

    10. Ensure that each combination is coherent and has a logical flow. The selected attribute values should complement each other, creating a cohesive and practical solution.

    11. Consider the impact of your combinations on various stakeholders, including end-users, businesses, society, and the environment. Incorporate attributes that address sustainability, inclusivity, and ethical considerations when relevant.

    12. Present your combinations in a clear and engaging writing style that effectively communicates your ideas and insights. Provide sufficient context and explanations to make the response informative and valuable to the reader.

    13. Conclude your Attribute Analysis with a summary of the key insights gained and the potential impact of the innovative combinations on the chosen product, service, or technology.

    '''
    return llm.generate_response(prompt)

# Streamlit app
def main():
    st.title("Market Analysis Generator")

    specific_offering = st.text_input("Enter the specific offering (e.g., 'ev battery'): ")

    if st.button("Generate Analysis"):
        if specific_offering:
            with st.spinner("Generating analysis..."):
                analysis = generate_analysis(specific_offering)
                st.markdown(analysis)
        else:
            st.warning("Please enter a specific offering.")

if __name__ == "__main__":
    main()

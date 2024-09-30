import streamlit as st 
import PyPDF2


def merge_pdfs(output_path, pdf_documents):
    
    pdf_merger = PyPDF2.PdfMerger()
    
    for pdf_document in pdf_documents:
        pdf_merger.append(pdf_document)
        
    with open(output_path, 'wb') as ouput_file:
        pdf_merger.write(ouput_file)
        pdf_merger.close()

def main():
    
    st.image('assets/unirpdfimg.png')
    st.header('Fusion de PDF')
    st.subheader('Adjunte archivos PDF para combinar')
    
    attached_pdfs = st.file_uploader(label="", accept_multiple_files=True, type='pdf')
    
    merg_button = st.button(label="Fusionar Archivos PDF")
    
    if merg_button:
        if len(attached_pdfs) <= 1:
            st.warning("Adjunte mas de un PDF para fusionarlo")
        else:
            output_pdf = 'assets/pdf_final.pdf'
            merge_pdfs(output_pdf, attached_pdfs)
            st.success("Los archivos PDF se fusionaron correctamente")
            
            with open(output_pdf, 'rb') as file:
                pdf_data = file.read()
            st.download_button(label="Descargar PDF fusionado", data=pdf_data, file_name='pdf_final.pdf')
            
if __name__ == "__main__":
    main()
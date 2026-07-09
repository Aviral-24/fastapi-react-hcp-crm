import { createSlice } from '@reduxjs/toolkit';

const initialState = {
  formData: {
    hcp_name: '',
    interaction_type: 'Meeting',
    date: new Date().toISOString().split('T')[0],
    // Time format fixed for HTML input compatibility (HH:mm in 24-hour format)
    time: new Date().toTimeString().slice(0, 5),
    topics: '',
    sentiment: '',
    materials_shared: []
  },
  messages: [
    { role: 'ai', content: 'Log interaction details here (e.g., "Met Dr. Smith, discussed Product X efficacy, positive sentiment, shared brochure") or ask for help.' }
  ],
  isLoading: false
};

const interactionSlice = createSlice({
  name: 'interaction',
  initialState,
  reducers: {
    addMessage: (state, action) => {
      state.messages.push(action.payload);
    },
    updateFormData: (state, action) => {
      // API se aane wale data ko parse aur update karein
      const data = action.payload;
      if (data.hcp_name) state.formData.hcp_name = data.hcp_name;
      if (data.topics) state.formData.topics = data.topics;
      if (data.sentiment) state.formData.sentiment = data.sentiment;
      
      // Handle stringified JSON for materials
      if (data.materials_shared) {
        try {
          state.formData.materials_shared = typeof data.materials_shared === 'string' 
            ? JSON.parse(data.materials_shared) 
            : data.materials_shared;
        } catch (e) {
          state.formData.materials_shared = [data.materials_shared];
        }
      }
    },
    setLoading: (state, action) => {
      state.isLoading = action.payload;
    }
  }
});

export const { addMessage, updateFormData, setLoading } = interactionSlice.actions;
export default interactionSlice.reducer;
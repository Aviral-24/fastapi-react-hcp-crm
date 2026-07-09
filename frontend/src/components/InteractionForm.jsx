import React from 'react';
import { useSelector } from 'react-redux';

export default function InteractionForm() {
  const { formData } = useSelector((state) => state.interaction);

  return (
    <div className="form-container">
      <h2>Log HCP Interaction</h2>
      <div className="form-grid">
        <div className="form-group">
          <label>HCP Name</label>
          <input type="text" value={formData.hcp_name} readOnly placeholder="Auto-filled by AI..." />
        </div>
        <div className="form-group">
          <label>Interaction Type</label>
          <select value={formData.interaction_type} disabled>
            <option>Meeting</option>
            <option>Call</option>
            <option>Email</option>
          </select>
        </div>
        <div className="form-group">
          <label>Date</label>
          <input type="date" value={formData.date} readOnly />
        </div>
        <div className="form-group">
          <label>Time</label>
          <input type="time" value={formData.time} readOnly />
        </div>
      </div>

      <div className="form-group full-width">
        <label>Topics Discussed</label>
        <textarea value={formData.topics} readOnly placeholder="Key discussion points..." rows="3" />
      </div>

      <div className="form-group full-width">
        <label>Materials Shared / Samples Distributed</label>
        <div className="tags-container">
          {formData.materials_shared.length > 0 ? (
            formData.materials_shared.map((item, index) => (
              <span key={index} className="tag">{item}</span>
            ))
          ) : (
            <span className="no-data">No materials added</span>
          )}
        </div>
      </div>

      <div className="form-group full-width">
        <label>Observed/Inferred HCP Sentiment</label>
        <div className="radio-group">
          <label>
            <input type="radio" checked={formData.sentiment?.toLowerCase() === 'positive'} readOnly /> Positive
          </label>
          <label>
            <input type="radio" checked={formData.sentiment?.toLowerCase() === 'neutral'} readOnly /> Neutral
          </label>
          <label>
            <input type="radio" checked={formData.sentiment?.toLowerCase() === 'negative'} readOnly /> Negative
          </label>
        </div>
      </div>
    </div>
  );
}
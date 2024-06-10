-- Creates Index of first initials and score
CREATE INDEX idx_name_first_score ON names (name(1), score);

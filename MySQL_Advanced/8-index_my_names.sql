-- Creates an index of first initials
CREATE INDEX idx_name_first ON names (name(1));

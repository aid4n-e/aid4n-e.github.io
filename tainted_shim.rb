# Local preview only: Ruby 3.2+ removed String#tainted?, which Liquid 4.0.3 still calls.
class Object
  def tainted?
    false
  end

  def untaint
    self
  end
end
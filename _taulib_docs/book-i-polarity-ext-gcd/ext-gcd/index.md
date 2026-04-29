---
{
  "projection_kind": "taulib_declaration",
  "title": "ext_gcd",
  "permalink": "/verify/taulib/docs/book-i-polarity-ext-gcd/ext-gcd/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.ExtGCD`.",
  "declaration_id": "TauLib.BookI.Polarity.ExtGCD::ext_gcd",
  "declaration_slug": "ext-gcd",
  "kind": "def",
  "name": "ext_gcd",
  "module_name": "TauLib.BookI.Polarity.ExtGCD",
  "module_url": "/verify/taulib/docs/book-i-polarity-ext-gcd/",
  "source_line_start": 27,
  "source_line_end": 33,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L27-L33",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.ExtGCD",
        "url": "/verify/taulib/docs/book-i-polarity-ext-gcd/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L27-L33",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookI.Polarity.ExtGCD](/verify/taulib/docs/book-i-polarity-ext-gcd/)
- Source path: [`TauLib/BookI/Polarity/ExtGCD.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/ExtGCD.lean#L27-L33)
- Source range: L27-L33
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Extended GCD: returns (gcd, s, t) with gcd = Nat.gcd a b
    and ↑a * s + ↑b * t = ↑gcd (Int coefficients). -/
```

## Source Excerpt

```lean
def ext_gcd (a b : Nat) : Nat × Int × Int :=
  if b = 0 then (a, 1, 0)
  else
    let r := ext_gcd b (a % b)
    (r.1, r.2.2, r.2.1 - ↑(a / b) * r.2.2)
termination_by b
decreasing_by exact Nat.mod_lt a (by omega)
```

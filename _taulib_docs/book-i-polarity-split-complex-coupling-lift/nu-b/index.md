---
{
  "projection_kind": "taulib_declaration",
  "title": "nuB",
  "permalink": "/corpus/taulib/docs/book-i-polarity-split-complex-coupling-lift/nu-b/",
  "summary_short": "`def` declaration in `TauLib.BookI.Polarity.SplitComplexCouplingLift`.",
  "declaration_id": "TauLib.BookI.Polarity.SplitComplexCouplingLift::nuB",
  "declaration_slug": "nu-b",
  "kind": "def",
  "name": "nuB",
  "module_name": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
  "module_url": "/corpus/taulib/docs/book-i-polarity-split-complex-coupling-lift/",
  "source_line_start": 293,
  "source_line_end": 293,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L293-L293",
  "formal_status": "defined",
  "declaration_role": "data/computed value",
  "formal_status_label": "data/computed value",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.SplitComplexCouplingLift",
        "url": "/corpus/taulib/docs/book-i-polarity-split-complex-coupling-lift/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L293-L293",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "data/computed value",
      "status": "data/computed value"
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

- Module: [TauLib.BookI.Polarity.SplitComplexCouplingLift](/corpus/taulib/docs/book-i-polarity-split-complex-coupling-lift/)
- Source path: [`TauLib/BookI/Polarity/SplitComplexCouplingLift.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/SplitComplexCouplingLift.lean#L293-L293)
- Source range: L293-L293
- Kind: `def`
- Public role: `data/computed value`
- Formal status hint: `data/computed value`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Counts the number of B-prime factors of `n` with multiplicity**
    (paper's `ν_B(n)`).

    **Wave 17 structural placeholder**: returns 0 for all inputs.
    The concrete prime-factorisation-based definition lives in
    Wave 18 alongside the Legendre `B_class` instantiation.  The
    Wave 17 placeholder is sufficient to land the structural
    type signatures + ramification triviality at the trace level. -/
```

## Source Excerpt

```lean
def nuB (_B_class : Nat → Bool) (_n : Nat) : Nat := 0
```

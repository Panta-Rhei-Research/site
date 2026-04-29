---
{
  "projection_kind": "taulib_declaration",
  "title": "omega_left_distrib",
  "permalink": "/verify/taulib/docs/book-i-polarity-omega-ring/omega-left-distrib/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Polarity.OmegaRing`.",
  "declaration_id": "TauLib.BookI.Polarity.OmegaRing::omega_left_distrib",
  "declaration_slug": "omega-left-distrib",
  "kind": "theorem",
  "name": "omega_left_distrib",
  "module_name": "TauLib.BookI.Polarity.OmegaRing",
  "module_url": "/verify/taulib/docs/book-i-polarity-omega-ring/",
  "source_line_start": 310,
  "source_line_end": 313,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L310-L313",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Polarity.OmegaRing",
        "url": "/verify/taulib/docs/book-i-polarity-omega-ring/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L310-L313",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookI.Polarity.OmegaRing](/verify/taulib/docs/book-i-polarity-omega-ring/)
- Source path: [`TauLib/BookI/Polarity/OmegaRing.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Polarity/OmegaRing.lean#L310-L313)
- Source range: L310-L313
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Distributivity: a * (b + c) = a*b + a*c (on omega-tails). -/
```

## Source Excerpt

```lean
theorem omega_left_distrib (n1 n2 n3 d : TauIdx) :
    (mk_omega_tail_mul n1 (n2 + n3) d).components =
    (mk_omega_tail_add (n1 * n2) (n1 * n3) d).components := by
  rw [omega_mul_components_eq, omega_add_components_eq, Nat.left_distrib]
```

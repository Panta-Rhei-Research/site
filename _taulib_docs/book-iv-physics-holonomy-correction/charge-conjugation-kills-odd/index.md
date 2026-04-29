---
{
  "projection_kind": "taulib_declaration",
  "title": "charge_conjugation_kills_odd",
  "permalink": "/verify/taulib/docs/book-iv-physics-holonomy-correction/charge-conjugation-kills-odd/",
  "summary_short": "`theorem` declaration in `TauLib.BookIV.Physics.HolonomyCorrection`.",
  "declaration_id": "TauLib.BookIV.Physics.HolonomyCorrection::charge_conjugation_kills_odd",
  "declaration_slug": "charge-conjugation-kills-odd",
  "kind": "theorem",
  "name": "charge_conjugation_kills_odd",
  "module_name": "TauLib.BookIV.Physics.HolonomyCorrection",
  "module_url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/",
  "source_line_start": 279,
  "source_line_end": 283,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L279-L283",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookIV.Physics.HolonomyCorrection",
        "url": "/verify/taulib/docs/book-iv-physics-holonomy-correction/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L279-L283",
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

- Module: [TauLib.BookIV.Physics.HolonomyCorrection](/verify/taulib/docs/book-iv-physics-holonomy-correction/)
- Source path: [`TauLib/BookIV/Physics/HolonomyCorrection.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookIV/Physics/HolonomyCorrection.lean#L279-L283)
- Source range: L279-L283
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Charge conjugation kills odd orders in the holonomy expansion.

    C: α → −α maps the U(1) connection on sector B.
    For a C-even observable (neutron mass, Q=0):
      Hol(A) = Σ (iα)^k/k! · (∮A)^k
      C[Hol(A)] = Σ (-iα)^k/k! · (∮A)^k
    Average (Hol + C[Hol])/2 retains only even-k terms.
    Leading correction: k=2, giving α². -/
```

## Source Excerpt

```lean
theorem charge_conjugation_kills_odd :
    -- The surviving order is 2 (even), the killed order is 1 (odd)
    -- The parity constraint: even orders survive C-averaging
    (2 : Nat) % 2 = 0 ∧ (1 : Nat) % 2 = 1 := by
  exact ⟨rfl, rfl⟩
```

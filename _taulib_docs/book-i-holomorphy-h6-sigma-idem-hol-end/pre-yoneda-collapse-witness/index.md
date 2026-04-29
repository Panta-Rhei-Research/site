---
{
  "projection_kind": "taulib_declaration",
  "title": "pre_yoneda_collapse_witness",
  "permalink": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/pre-yoneda-collapse-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd`.",
  "declaration_id": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd::pre_yoneda_collapse_witness",
  "declaration_slug": "pre-yoneda-collapse-witness",
  "kind": "theorem",
  "name": "pre_yoneda_collapse_witness",
  "module_name": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
  "module_url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/",
  "source_line_start": 258,
  "source_line_end": 261,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L258-L261",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd",
        "url": "/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L258-L261",
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

- Module: [TauLib.BookI.Holomorphy.H6SigmaIdemHolEnd](/verify/taulib/docs/book-i-holomorphy-h6-sigma-idem-hol-end/)
- Source path: [`TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/H6SigmaIdemHolEnd.lean#L258-L261)
- Source range: L258-L261
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §9 Pre-Yoneda Collapse — structural witness via
    Wave 26 (Hinge 7) canonical-address NF**.

    The pre-Yoneda collapse claims every τ-carrier embeds
    concretely into the boundary `∂τC³` of Hinge 1.  In TauLib
    this concrete embedding is provided by Wave 26's
    canonical-address normalization: every Program (codeable
    transformer) has a unique canonical NormalForm via
    `normalize`.

    The statement-witness form: every Program is
    canonically-addressable via Wave 26's `normalize` map. -/
```

## Source Excerpt

```lean
theorem pre_yoneda_collapse_witness (p : Program) :
    -- Every Program has a canonical NF address (Wave 26)
    ∃ nf : NormalForm, normalize p = nf :=
  ⟨normalize p, rfl⟩
```

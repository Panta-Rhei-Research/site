---
{
  "projection_kind": "taulib_declaration",
  "title": "classical_topos_subquotient_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-classical-closure/classical-topos-subquotient-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ClassicalClosure`.",
  "declaration_id": "TauLib.BookI.Topos.H7ClassicalClosure::classical_topos_subquotient_witness",
  "declaration_slug": "classical-topos-subquotient-witness",
  "kind": "theorem",
  "name": "classical_topos_subquotient_witness",
  "module_name": "TauLib.BookI.Topos.H7ClassicalClosure",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/",
  "source_line_start": 126,
  "source_line_end": 129,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L126-L129",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.H7ClassicalClosure",
        "url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L126-L129",
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

- Module: [TauLib.BookI.Topos.H7ClassicalClosure](/verify/taulib/docs/book-i-topos-h7-classical-closure/)
- Source path: [`TauLib/BookI/Topos/H7ClassicalClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L126-L129)
- Source range: L126-L129
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §8 Thm `classical-topos-subquotient` — structural witness**.

    The classical subquotient Cat_τ^cl (= Cat_τ / ∼_cl) has
    two-valued classifier Ω_cl = {0, 1}, captured at the
    Truth4 level by the {T, F} ⊆ Truth4 inclusion.

    Concrete witness: T and F are distinct in Truth4
    (`Truth4.noConfusion`), forming the classical
    {0, 1} subquotient. -/
```

## Source Excerpt

```lean
theorem classical_topos_subquotient_witness :
    -- T and F are distinct in Truth4 (the classical {0, 1})
    (T : Truth4) ≠ F := by
  decide
```

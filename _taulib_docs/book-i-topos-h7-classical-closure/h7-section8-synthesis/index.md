---
{
  "projection_kind": "taulib_declaration",
  "title": "h7_section8_synthesis",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-classical-closure/h7-section8-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ClassicalClosure`.",
  "declaration_id": "TauLib.BookI.Topos.H7ClassicalClosure::h7_section8_synthesis",
  "declaration_slug": "h7-section8-synthesis",
  "kind": "theorem",
  "name": "h7_section8_synthesis",
  "module_name": "TauLib.BookI.Topos.H7ClassicalClosure",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/",
  "source_line_start": 178,
  "source_line_end": 187,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L178-L187",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L178-L187",
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
- Source path: [`TauLib/BookI/Topos/H7ClassicalClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L178-L187)
- Source range: L178-L187
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Wave 33 H7 §8 synthesis**.

    Three structural clauses for paper §8:

    1. **§8 Classical-topos subquotient**: T ≠ F in Truth4
       (the classical {0, 1} subclassifier).

    2. **§8 Classical embedding**: classical topos theory embeds
       in Cat_τ + Truth4 has non-classical values B, N.

    3. **§8 Comparison functor**: B truncates up to T, N down
       to F (canonical π_cl truncation). -/
```

## Source Excerpt

```lean
theorem h7_section8_synthesis :
    -- Clause 1: classical {0, 1} subclassifier
    ((T : Truth4) ≠ F) ∧
    -- Clause 2: extra non-classical values exist
    (∃ v : Truth4, v ≠ T ∧ v ≠ F) ∧
    -- Clause 3: canonical truncations
    (Truth4.join B T = T ∧ Truth4.meet N F = F) :=
  ⟨classical_topos_subquotient_witness,
   classical_subquotient_witness,
   comparison_functor_structural_witness⟩
```

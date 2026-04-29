---
{
  "projection_kind": "taulib_declaration",
  "title": "classical_embedding_witness",
  "permalink": "/verify/taulib/docs/book-i-topos-h7-classical-closure/classical-embedding-witness/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.H7ClassicalClosure`.",
  "declaration_id": "TauLib.BookI.Topos.H7ClassicalClosure::classical_embedding_witness",
  "declaration_slug": "classical-embedding-witness",
  "kind": "theorem",
  "name": "classical_embedding_witness",
  "module_name": "TauLib.BookI.Topos.H7ClassicalClosure",
  "module_url": "/verify/taulib/docs/book-i-topos-h7-classical-closure/",
  "source_line_start": 139,
  "source_line_end": 142,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L139-L142",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L139-L142",
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
- Source path: [`TauLib/BookI/Topos/H7ClassicalClosure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/H7ClassicalClosure.lean#L139-L142)
- Source range: L139-L142
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper §8 Thm `classical-embedding` — structural witness**.

    Classical topos theory embeds in Cat_τ via {T, F} ⊆ Truth4.
    The four-valued Truth4 strictly extends classical {0, 1}:
    B and N witness the *non-classical* extra structure.

    Direct witness via Wave 31's `classical_subquotient_witness`:
    there exists v ∈ Truth4 with v ≠ T ∧ v ≠ F (namely B or N). -/
```

## Source Excerpt

```lean
theorem classical_embedding_witness :
    -- {T, F} embeds in Truth4 + Truth4 has extra non-classical values
    ((T : Truth4) ≠ F) ∧ (∃ v : Truth4, v ≠ T ∧ v ≠ F) :=
  ⟨by decide, classical_subquotient_witness⟩
```

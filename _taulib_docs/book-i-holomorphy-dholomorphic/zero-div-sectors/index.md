---
{
  "projection_kind": "taulib_declaration",
  "title": "zero_div_sectors",
  "permalink": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/zero-div-sectors/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Holomorphy.DHolomorphic`.",
  "declaration_id": "TauLib.BookI.Holomorphy.DHolomorphic::zero_div_sectors",
  "declaration_slug": "zero-div-sectors",
  "kind": "theorem",
  "name": "zero_div_sectors",
  "module_name": "TauLib.BookI.Holomorphy.DHolomorphic",
  "module_url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/",
  "source_line_start": 127,
  "source_line_end": 128,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L127-L128",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Holomorphy.DHolomorphic",
        "url": "/corpus/taulib/docs/book-i-holomorphy-dholomorphic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L127-L128",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Holomorphy.DHolomorphic](/corpus/taulib/docs/book-i-holomorphy-dholomorphic/)
- Source path: [`TauLib/BookI/Holomorphy/DHolomorphic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Holomorphy/DHolomorphic.lean#L127-L128)
- Source range: L127-L128
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- e₊ · e₋ = 0: the zero divisor product in sector coordinates.
    This is the fundamental pathology of D-holomorphy:
    functions can be zero on one sector and arbitrary on the other. -/
```

## Source Excerpt

```lean
theorem zero_div_sectors : SectorPair.mul e_plus_sector e_minus_sector = ⟨0, 0⟩ :=
  e_orthogonal
```

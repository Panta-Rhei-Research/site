---
{
  "projection_kind": "taulib_declaration",
  "title": "TauRatQ.toRat",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/to-rat/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.Bridge.TauRatQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRatQuotient::TauRatQ.toRat",
  "declaration_slug": "to-rat",
  "kind": "def",
  "name": "TauRatQ.toRat",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
  "module_url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/",
  "source_line_start": 80,
  "source_line_end": 84,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L80-L84",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRatQuotient",
        "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L80-L84",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "role": "definition",
      "status": "definition"
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRatQuotient](/corpus/taulib/docs/book-i-boundary-bridge-tau-rat-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRatQuotient.lean#L80-L84)
- Source range: L80-L84
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Lift `TauRat.toRat` to the quotient. -/
```

## Source Excerpt

```lean
def TauRatQ.toRat : TauRatQ → Rat :=
  Quotient.lift TauRat.toRat (fun a b h => (equiv_iff_toRat_eq a b).mp h)

@[simp] theorem TauRatQ.toRat_mk (a : TauRat) :
    TauRatQ.toRat a.toQ = a.toRat := rfl
```

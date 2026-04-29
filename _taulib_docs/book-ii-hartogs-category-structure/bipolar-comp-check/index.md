---
{
  "projection_kind": "taulib_declaration",
  "title": "bipolar_comp_check",
  "permalink": "/verify/taulib/docs/book-ii-hartogs-category-structure/bipolar-comp-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Hartogs.CategoryStructure`.",
  "declaration_id": "TauLib.BookII.Hartogs.CategoryStructure::bipolar_comp_check",
  "declaration_slug": "bipolar-comp-check",
  "kind": "def",
  "name": "bipolar_comp_check",
  "module_name": "TauLib.BookII.Hartogs.CategoryStructure",
  "module_url": "/verify/taulib/docs/book-ii-hartogs-category-structure/",
  "source_line_start": 363,
  "source_line_end": 380,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L363-L380",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Hartogs.CategoryStructure",
        "url": "/verify/taulib/docs/book-ii-hartogs-category-structure/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L363-L380",
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

- Module: [TauLib.BookII.Hartogs.CategoryStructure](/verify/taulib/docs/book-ii-hartogs-category-structure/)
- Source path: [`TauLib/BookII/Hartogs/CategoryStructure.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Hartogs/CategoryStructure.lean#L363-L380)
- Source range: L363-L380
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Composition respects bipolar decomposition:
    the B-sector and C-sector compose independently.
    For StageFun composition: (f.g).b = f.b . g.b, (f.g).c = f.c . g.c.
    This is structural from the definition of StageFun.comp. -/
```

## Source Excerpt

```lean
def bipolar_comp_check (bound db : TauIdx) : Bool :=
  go 2 1 ((bound + 1) * (db + 1))
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Check that StageFun.comp respects sectors
      let f := chi_plus_stage
      let g := id_stage
      let comp := StageFun.comp f g
      -- B-sector: comp.b = f.b(g.b(x, k), k)
      let b_ok := comp.b_fun x k == f.b_fun (g.b_fun x k) k
      -- C-sector: comp.c = f.c(g.c(x, k), k)
      let c_ok := comp.c_fun x k == f.c_fun (g.c_fun x k) k
      b_ok && c_ok && go x (k + 1) (fuel - 1)
  termination_by fuel
```

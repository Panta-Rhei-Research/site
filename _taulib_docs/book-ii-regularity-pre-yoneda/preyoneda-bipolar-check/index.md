---
{
  "projection_kind": "taulib_declaration",
  "title": "preyoneda_bipolar_check",
  "permalink": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/preyoneda-bipolar-check/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.PreYoneda`.",
  "declaration_id": "TauLib.BookII.Regularity.PreYoneda::preyoneda_bipolar_check",
  "declaration_slug": "preyoneda-bipolar-check",
  "kind": "def",
  "name": "preyoneda_bipolar_check",
  "module_name": "TauLib.BookII.Regularity.PreYoneda",
  "module_url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/",
  "source_line_start": 154,
  "source_line_end": 171,
  "registry_ids": [
    "II.P11"
  ],
  "related_registry_items": [
    {
      "id": "II.P11",
      "title": "Hom Bipolar Decomposition",
      "url": "/registry/object/II.P11/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L154-L171",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.PreYoneda",
        "url": "/verify/taulib/docs/book-ii-regularity-pre-yoneda/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L154-L171",
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

- Module: [TauLib.BookII.Regularity.PreYoneda](/verify/taulib/docs/book-ii-regularity-pre-yoneda/)
- Source path: [`TauLib/BookII/Regularity/PreYoneda.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/PreYoneda.lean#L154-L171)
- Source range: L154-L171
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.P11` — Hom Bipolar Decomposition

## Immediate Comment / Docstring

```lean
/-- [II.P11] Bipolar structure of the pre-Yoneda embedding:
    the B-channel and C-channel of the embedded function decompose
    independently.

    For a function f, the pre-Yoneda image has bipolar coordinates:
    - B-channel: from_tau_idx(preyoneda(f, x, k)).b
    - C-channel: from_tau_idx(preyoneda(f, x, k)).c

    We verify that the bipolar decomposition is consistent:
    the sector pair from interior_bipolar applied to the embedded
    point decomposes into e_plus and e_minus projections that
    recombine to give the full sector pair. -/
```

## Source Excerpt

```lean
def preyoneda_bipolar_check (bound db : TauIdx) : Bool :=
  go 2 1 (bound * db + bound + db + 1)
where
  go (x k fuel : Nat) : Bool :=
    if fuel = 0 then true
    else if x > bound then true
    else if k > db then go (x + 1) 1 (fuel - 1)
    else
      -- Embed the identity function: preyoneda(id, x, k) = reduce(x, k)
      let embedded := reduce x k
      let p := from_tau_idx embedded
      let sp := interior_bipolar p
      -- Bipolar decomposition: e_plus projection + e_minus projection = full
      let proj_b := SectorPair.mul e_plus_sector sp
      let proj_c := SectorPair.mul e_minus_sector sp
      let recombined := SectorPair.add proj_b proj_c
      (recombined == sp) && go x (k + 1) (fuel - 1)
  termination_by fuel
```

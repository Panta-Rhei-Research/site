---
{
  "projection_kind": "taulib_declaration",
  "title": "pred_sgra_outflow_angle",
  "permalink": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/pred-sgra-outflow-angle/",
  "summary_short": "`def` declaration in `TauLib.BookV.Cosmology.FalsificationPack`.",
  "declaration_id": "TauLib.BookV.Cosmology.FalsificationPack::pred_sgra_outflow_angle",
  "declaration_slug": "pred-sgra-outflow-angle",
  "kind": "def",
  "name": "pred_sgra_outflow_angle",
  "module_name": "TauLib.BookV.Cosmology.FalsificationPack",
  "module_url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/",
  "source_line_start": 316,
  "source_line_end": 324,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L316-L324",
  "formal_status": "defined",
  "declaration_role": "definition",
  "formal_status_label": "definition",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Cosmology.FalsificationPack",
        "url": "/corpus/taulib/docs/book-v-cosmology-falsification-pack/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L316-L324",
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

- Module: [TauLib.BookV.Cosmology.FalsificationPack](/corpus/taulib/docs/book-v-cosmology-falsification-pack/)
- Source path: [`TauLib/BookV/Cosmology/FalsificationPack.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Cosmology/FalsificationPack.lean#L316-L324)
- Source range: L316-L324
- Kind: `def`
- Public role: `definition`
- Formal status hint: `definition`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- N16 (Q8): Sgr A* outflow opening half-angle ≤ 20° (V.T90 application).

    V.T90 Jet Collimation Theorem topological upper bound:
      θ_jet ≤ arcsin(ι_τ) ≈ 19.96°

    Anchor paper: Yusef-Zadeh et al. 2023, ApJL 949:L31, reports
    nominal half-opening angle θ ≈ 20° for Sgr A*'s degree-scale
    in-plane outflow. Sits at the τ-framework's topological ceiling.

    Caveats per Wave R15 Specialist α (1.5/5 observational rating):
    (i) the 20° is a NOMINAL model-fit value adopted in §4.3 to close
    ram-pressure balance, not a directly imaged opening angle;
    (ii) bar-orbit alternative (Wallace+2022) not defeated by the
    paper, only dismissed by scale-extrapolation;
    (iii) Sgr A* exhibits TWO distinct outflow geometries (in-plane
    vs vertical bipolar bubbles), τ-framework needs to specify
    which V.T90 applies to. -/
```

## Source Excerpt

```lean
def pred_sgra_outflow_angle : TestablePrediction where
  name := "Q8 (N16): Sgr A* outflow opening half-angle <= 20° (V.T90)"
  level := .Quantitative
  description :=
    "V.T90 Jet Collimation: theta_jet <= arcsin(iota_tau) ~ 19.96°. " ++
    "Falsifier: outflow opening half-angle measured > 25° at jet base " ++
    "refutes V.T110 + topological bound."
  status := "Currently testable: VLBI/MeerKAT measurements ongoing."
  currently_testable := true
```
